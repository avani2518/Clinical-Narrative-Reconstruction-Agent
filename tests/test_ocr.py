from src.ocr.ocr_engine import OCREngine

ocr = OCREngine()

text = ocr.extract_text(
    "data/images/sample_prescription.jpg"
)

print(text)