from pathlib import Path

import fitz  # PyMuPDF
from docx import Document


class CVService:

    @staticmethod
    def extract_pdf(file_path: str) -> str:

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    @staticmethod
    def extract_docx(file_path: str) -> str:

        doc = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    @staticmethod
    def read_cv(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return CVService.extract_pdf(file_path)

        elif extension == ".docx":
            return CVService.extract_docx(file_path)

        raise ValueError("Formato no soportado.")