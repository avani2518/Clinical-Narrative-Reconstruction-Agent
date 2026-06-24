import os

from src.ner.entity_extractor import EntityExtractor
from src.timeline.reconstructor import TimelineReconstructor


extractor = EntityExtractor()
reconstructor = TimelineReconstructor()

reports = []

folder = "data/raw"

for filename in os.listdir(folder):

    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    reports.append(extractor.extract(text))


timeline = reconstructor.build_timeline(reports)

for event in timeline:

    print("\n===================")

    print(event["date"].strftime("%d-%m-%Y"))

    print("Diagnoses:", event["diagnoses"])

    print("Medications:", event["medications"])

    print("Labs:", event["lab_results"])