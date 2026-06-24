from transformers import pipeline


class MedicalNER:

    def __init__(self):

        self.ner = pipeline(
            "token-classification",
            model="samrawal/bert-base-uncased_clinical-ner",
            aggregation_strategy="simple"
        )

    def extract(self, text):

        entities = self.ner(text)

        return entities