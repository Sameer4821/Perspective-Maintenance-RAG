from pathlib import Path
import fitz  # PyMuPDF

class DocumentLoader:
    def __init__(self, folder="data/manuals"):
        self.folder = Path(folder)

    def load_documents(self):
        documents = []

        for pdf in self.folder.glob("*.pdf"):
            doc = fitz.open(pdf)

            text = ""
            for page in doc:
                text += page.get_text()

            documents.append({
                "file_name": pdf.name,
                "content": text
            })

        return documents