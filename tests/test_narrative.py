import os

from src.ner.entity_extractor import EntityExtractor
from src.timeline.reconstructor import TimelineReconstructor
from src.output.narrative_generator import NarrativeGenerator

extractor = EntityExtractor()
timeline_builder = TimelineReconstructor()
generator = NarrativeGenerator()

reports = []

for filename in os.listdir("data/raw"):

    filepath = os.path.join("data/raw", filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    reports.append(extractor.extract(text))

timeline = timeline_builder.build_timeline(reports)

summary = generator.generate(timeline)

print(summary)