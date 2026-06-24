from src.pdf.pdf_reader import PDFReader

reader = PDFReader()

text = reader.extract_text(
    "data/images/VANI.pdf"
)

print(text)