import os
import PyPDF2
from docx import Document

class FileLoader:
    @staticmethod
    def load_file(path):
        if not os.path.isfile(path):
            raise FileNotFoundError("Invalid file path")

        ext = os.path.splitext(path)[1].lower()

        if ext == ".txt":
            return FileLoader._load_txt(path)
        elif ext == ".pdf":
            return FileLoader._load_pdf(path)
        elif ext == ".docx":
            return FileLoader._load_docx(path)
        else:
            raise ValueError("Unsupported file type")

    @staticmethod
    def _load_txt(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def _load_pdf(path):
        text = ""
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += (page.extract_text() or "") + "\n"
        return text

    @staticmethod
    def _load_docx(path):
        doc = Document(path)
        return "\n".join(para.text for para in doc.paragraphs)
