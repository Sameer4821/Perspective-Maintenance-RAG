from app.services.pdf_parser import PDFParser

documents = PDFParser.load_pdf("data/manuals/sample_manual.pdf")

print(f"Total Pages: {len(documents)}")

print("\nFirst Page:\n")
print(documents[0].page_content)