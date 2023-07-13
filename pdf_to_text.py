import os
from pdfminer.high_level import extract_text

def convert_pdf_to_txt(pdf_path, txt_path):
    text = extract_text(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

# directories with PDFs
directories = [
    "C:/Users/Fonck/Documents/SuperStonk",
    "C:/Users/Fonck/Documents/SuperStonk/GME Quaterly reports"
]

# directory to save text files
output_dir = "C:/Users/Fonck/Documents/SuperStonk/TextFiles"

# create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for directory in directories:
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            txt_filename = os.path.splitext(filename)[0] + ".txt"  # change .pdf to .txt
            txt_path = os.path.join(output_dir, txt_filename)
            convert_pdf_to_txt(pdf_path, txt_path)
