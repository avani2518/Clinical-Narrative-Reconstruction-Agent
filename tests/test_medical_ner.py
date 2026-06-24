from src.ner.medical_ner import MedicalNER

model = MedicalNER()

text = """
Patient has Type 2 Diabetes.
Currently taking Metformin 500mg twice daily.
HbA1c is 8.2%.
"""

entities = model.extract(text)

for e in entities:
    print(e)