<<<<<<< HEAD
\
# 🧾 AI-Powered Handwritten Sales Bill Digitization and Seamless Accounting Integration for MSMEs

## 📘 Abstract
Small retailers and shopkeepers in emerging markets still rely heavily on handwritten sales bills and manually enter purchase invoices into accounting software such as **BUSY** — a process that is slow, error-prone, and inefficient.

This project introduces an **AI-powered mobile and web platform** designed to **digitize handwritten and printed sales bills**, extract structured data using **OCR (Optical Character Recognition)** and **NLP (Natural Language Processing)**, and **seamlessly integrate** the data with BUSY accounting software.

The system supports **handwriting recognition, abbreviation expansion (e.g., “p oil” → “palm oil”)**, multilingual processing, and a **human-in-the-loop review interface** to ensure high accuracy.  
Ultimately, it helps MSMEs transition toward digital operations without disrupting their existing workflows.

## 🚀 Key Features
- Image capture & upload (mobile/web)
- OCR using EasyOCR/TrOCR/Tesseract
- NLP-based extraction and abbreviation normalization
- Human-in-the-loop review UI
- Export to CSV/XLSX compatible with BUSY

## ⚙️ Quick Start (local development)
1. Clone the repository
```bash
git clone https://github.com/<your-username>/AI-Bill-Digitizer.git
cd AI-Bill-Digitizer
```
2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
```
3. Run the backend API
```bash
uvicorn app:app --reload --port 8000
```
Open http://localhost:8000/docs for API docs (Swagger UI).

---
## 📁 Included files
- `app.py` — FastAPI backend with an `/upload` endpoint (placeholder OCR pipeline).
- `requirements.txt` — Python dependencies.
- `frontend/index.html` — Minimal web page to upload an image and preview results.
- `abbrev_dict.json` — Sample editable abbreviation dictionary.
- `sample_data/` — Folder for sample bill images and example outputs.
- `scripts/export_to_busy.py` — Example exporter from extracted data to BUSY-compatible CSV/XLSX.
- `README.md` — This file.

---
## 📜 License
Academic project for IEEE Mini Project Symposium — reuse with attribution.
=======
# AI_Bill_Digitizer
>>>>>>> 29e4cb12d960c98041a598f7b60e31617ed5db44
