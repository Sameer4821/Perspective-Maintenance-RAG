from app.services.pdf_parser import PDFParser
from app.services.text_chunker import TextChunker

# Load the PDF
documents = PDFParser.load_pdf("data/manuals/sample_manual.pdf")

# Split into chunks
chunks = TextChunker.chunk_documents(documents)

# Print results
print("=" * 50)
print(f"Total Chunks: {len(chunks)}")
print("=" * 50)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 30)
    print(chunk.page_content)
    print("\nMetadata:", chunk.metadata)