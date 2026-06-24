from src.ner.medical_ner import MedicalNER


class ClinicalEntityExtractor:

    def __init__(self):

        self.model = MedicalNER()

    def extract(self, text):

        ner_results = self.model.extract(text)

        structured = {
            "diagnoses": [],
            "medications": [],
            "tests": []
        }

        for entity in ner_results:

            entity_type = entity["entity_group"]
            entity_text = entity["word"]

            if entity_type == "problem":
                structured["diagnoses"].append(entity_text)

            elif entity_type == "treatment":
                structured["medications"].append(entity_text)

            elif entity_type == "test":
                structured["tests"].append(entity_text)

        return structured