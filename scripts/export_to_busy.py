import json, csv, pandas as pd
from pathlib import Path

def export_to_csv(extracted, out_file="busy_export.csv"):
    """
    Example: Accepts a list of item dicts and writes a BUSY-compatible CSV.
    Adjust column names to match BUSY import template.
    """
    df = pd.DataFrame(extracted)
    df.to_csv(out_file, index=False)
    print("Exported to", out_file)

if __name__ == "__main__":
    demo = [
        {"Item":"Palm Oil","Qty":"2 kg","Rate":340,"Amount":680},
    ]
    export_to_csv(demo, "busy_export.csv")
