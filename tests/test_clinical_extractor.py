from src.ner.clinical_entity_extractor import ClinicalEntityExtractor

extractor = ClinicalEntityExtractor()

text = """
Patient has Type 2 Diabetes.

Currently taking Metformin 500mg twice daily.

HbA1c is 8.2%.
"""

result = extractor.extract(text)

print(result)