import re

class EntityExtractor:

    def extract(self, text):

        entities = {
            "dates": [],
            "diagnoses": [],
            "medications": [],
            "lab_results": [],
            "allergies": []
        }

        # Date extraction
        date_pattern = r"\d{1,2}\s+[A-Za-z]+\s+\d{4}"
        entities["dates"] = re.findall(date_pattern, text)

        # Diagnoses
        if "Diabetes" in text:
            entities["diagnoses"].append("Type 2 Diabetes")

        if "Hypertension" in text:
            entities["diagnoses"].append("Hypertension")

        # Medications
        if "Metformin" in text:
            entities["medications"].append("Metformin")

        if "Amlodipine" in text:
            entities["medications"].append("Amlodipine")

        if "Amoxicillin" in text:
            entities["medications"].append("Amoxicillin")

        if "Penicillin" in text:
            entities["allergies"].append("Penicillin")
            

        # Lab Results
        hba1c_match = re.search(r"HbA1c:\s*([\d.]+)%", text)

        if hba1c_match:
            entities["lab_results"].append({
                "test": "HbA1c",
                "value": hba1c_match.group(1)
            })

        return entities