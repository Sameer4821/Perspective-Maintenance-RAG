from langchain_community.document_loaders import PyPDFLoader


class PDFParser:

    @staticmethod
    def load_pdf(file_path: str):
        """
        Load a PDF and return its pages.
        """
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        return documents