# pip install PyMuPDF

from pypdf import PdfReader
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def check_if_file_exists(filename):
    if os.path.exists(filename):
        return 1
    else:
        return 0

pdf_path = './data/pdf-files/sample-file.pdf'

file_exists = check_if_file_exists(pdf_path)

if file_exists:
    text = extract_text_from_pdf(pdf_path)
    print(text)
else:
    print ("Could not fild the PDF file!")