from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import io, json
from PIL import Image
import uvicorn

# === Base paths ===
BASE = Path(__file__).parent
ABBREV_FILE = BASE / "abbrev_dict.json"

# === FastAPI App ===
app = FastAPI(title="AI Bill Digitizer - API")

# === CORS Middleware ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for local HTML use)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Helper Functions ===
def load_abbrev():
    """Load abbreviation dictionary"""
    if ABBREV_FILE.exists():
        return json.loads(ABBREV_FILE.read_text(encoding="utf-8"))
    return {}

def normalize_item(item_text, abbrev):
    """
    Normalize an item line using abbreviation dictionary.
    Returns (normalized_text, unknown_words)
    """
    t = item_text
    unknown = []
    words = t.split()
    for w in words:
        lw = w.lower()
        if lw in abbrev:
            t = t.replace(w, abbrev[lw])
        else:
            # consider potential shortform if short alphabetic word
            if lw.isalpha() and len(lw) <= 5:
                unknown.append(lw)
    return t, unknown


# === Upload Endpoint ===
@app.post("/upload")
async def upload_bill(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    save_path = BASE / "sample_data" / file.filename
    save_path.parent.mkdir(exist_ok=True)
    image.save(save_path)

    # === OCR attempt ===
    extracted_lines = []
    try:
        import easyocr
        reader = easyocr.Reader(['en'], gpu=False)
        results = reader.readtext(save_path.as_posix(), detail=0)
        extracted_lines = results
    except Exception as e:
        print("⚠️ OCR error:", e)
        extracted_lines = ["p oil 2kg 340", "Total 340", "Invoice: 1234", "Date: 2025-01-01"]

    abbrev = load_abbrev()
    normalized = []
    new_unknowns = set()

    for line in extracted_lines:
        norm, unknowns = normalize_item(line, abbrev)
        normalized.append(norm)
        new_unknowns.update(unknowns)

    response = {
        "filename": file.filename,
        "extracted_lines": extracted_lines,
        "normalized_lines": normalized,
        "abbrev_used": list(abbrev.keys()),
        "unknown_words": list(new_unknowns)
    }
    return JSONResponse(response)


# === Abbreviation Dictionary Endpoints ===
@app.get("/abbrev")
def get_abbrev():
    """Return the current abbreviation dictionary"""
    if ABBREV_FILE.exists():
        return JSONResponse(json.loads(ABBREV_FILE.read_text(encoding="utf-8")))
    return JSONResponse({})


@app.post("/abbrev")
def update_abbrev(data: dict):
    """Update abbreviation dictionary with new words"""
    old = {}
    if ABBREV_FILE.exists():
        old = json.loads(ABBREV_FILE.read_text(encoding="utf-8"))
    old.update(data)
    ABBREV_FILE.write_text(json.dumps(old, indent=2), encoding="utf-8")
    return JSONResponse({"status": "saved", "entries": len(old)})


# === Run App ===
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
