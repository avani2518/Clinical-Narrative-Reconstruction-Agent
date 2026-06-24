class ContradictionDetector:

    def detect(self, timeline):

        alerts = []

        all_allergies = []
        all_medications = []

        for event in timeline:

            all_allergies.extend(event["allergies"])
            all_medications.extend(event["medications"])

        if "Penicillin" in all_allergies:

            for med in all_medications:

                if "Amoxicillin" in med:

                    alerts.append({
                        "severity": "CRITICAL",
                        "message": "Amoxicillin prescribed despite Penicillin allergy"
                    })

        return alerts