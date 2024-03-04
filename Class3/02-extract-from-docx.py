# pip install python-docx

from docx import Document
import os

def extract_text_from_docx(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


def check_if_file_exists(filename):
    if os.path.exists(filename):
        return 1
    else:
        return 0

filename = "./data/word-docs/doc-with-text.docx"
file_exists = check_if_file_exists(filename)

if file_exists:
    text = extract_text_from_docx(filename)
    print (text)
else:
    print ("Could not find the file")