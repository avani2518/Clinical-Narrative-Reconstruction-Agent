from datetime import datetime


class TimelineReconstructor:

    def build_timeline(self, extracted_reports):

        timeline = []

        for report in extracted_reports:

            date_str = report["dates"][0] if report["dates"] else "Unknown"

            try:
                date_obj = datetime.strptime(date_str, "%d %B %Y")
            except:
                try:
                    date_obj = datetime.strptime(date_str, "%d %b %Y")
                except:
                    continue

            timeline.append({
                "date": date_obj,
                "diagnoses": report["diagnoses"],
                "medications": report["medications"],
                "lab_results": report["lab_results"],
                "allergies": report["allergies"]
            })

        timeline.sort(key=lambda x: x["date"])

        return timeline