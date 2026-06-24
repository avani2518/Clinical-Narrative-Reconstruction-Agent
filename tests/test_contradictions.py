import os

from src.ner.entity_extractor import EntityExtractor
from src.timeline.reconstructor import TimelineReconstructor
from src.timeline.contradiction_detector import ContradictionDetector

extractor = EntityExtractor()
timeline_builder = TimelineReconstructor()
detector = ContradictionDetector()

reports = []

for filename in os.listdir("data/raw"):

    filepath = os.path.join("data/raw", filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    reports.append(extractor.extract(text))

timeline = timeline_builder.build_timeline(reports)

alerts = detector.detect(timeline)

for alert in alerts:

    print("\n========================")
    print(alert["severity"])
    print(alert["message"])