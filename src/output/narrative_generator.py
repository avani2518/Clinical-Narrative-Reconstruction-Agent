class NarrativeGenerator:

    def generate(self, timeline):

        narrative = []

        for event in timeline:

            date = event["date"].strftime("%B %Y")

            diagnoses = ", ".join(event["diagnoses"])
            medications = ", ".join(event["medications"])

            if diagnoses:

                text = f"In {date}, patient was diagnosed with {diagnoses}"

                if medications:
                    text += f" and started on {medications}"

                text += "."

                narrative.append(text)

            for lab in event["lab_results"]:

                narrative.append(
                    f"In {date}, {lab['test']} was recorded at {lab['value']}."
                )

        return "\n".join(narrative)