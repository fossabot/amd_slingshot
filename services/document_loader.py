# import os
# from config.settings import DATA_PATH

# def load_documents():
#     documents = []

#     for file in os.listdir(DATA_PATH):
#         file_path = os.path.join(DATA_PATH, file)

#         if file.endswith(".txt"):
#             with open(file_path, "r", encoding="utf-8") as f:
#                 documents.append(f.read())

#     return documents

import os
import pdfplumber
import docx
from config.settings import DATA_PATH


def load_pdf(file):
    """
    Extract text from a PDF file
    """
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def load_docx(file):
    """
    Extract text from a DOCX file
    """
    doc = docx.Document(file)

    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def load_text(file):
    """
    Extract text from TXT file
    """
    return file.read().decode("utf-8")


def load_documents():
    """
    Load framework documents from data/frameworks folder
    """
    documents = []

    for file in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, file)

        if file.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents