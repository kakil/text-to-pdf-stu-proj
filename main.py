import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("files/*txt")
print(filepaths)

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem.title()
    print(filename)
    pdf.add_page()
    pdf.set_font(family="Arial", size=18, style="B")
    pdf.cell(w=50, h=10, txt=f"{filename}")

    with open(filepath, 'r') as file:
        text = file.read()
        # pdf.set_font(family="Arial", size=12)
        # pdf.cell(w=10, h=20, txt=f"{text}")

pdf.output(f"PDFs/output.pdf")