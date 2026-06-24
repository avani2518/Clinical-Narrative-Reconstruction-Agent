import os

from src.ner.entity_extractor import EntityExtractor
from src.timeline.reconstructor import TimelineReconstructor
from src.output.narrative_generator import NarrativeGenerator
from src.timeline.contradiction_detector import ContradictionDetector

class ClinicalPipeline:

    def __init__(self):

        self.extractor = EntityExtractor()
        self.timeline_builder = TimelineReconstructor()
        self.narrative_generator = NarrativeGenerator()
        self.detector = ContradictionDetector()

    def process_folder(self, folder_path):

        reports = []

        for filename in os.listdir(folder_path):

            if not filename.endswith(".txt"):
                continue

            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            reports.append(
                self.extractor.extract(text)
            )

        timeline = self.timeline_builder.build_timeline(reports)

        narrative = self.narrative_generator.generate(timeline)

        alerts = self.detector.detect(timeline)

        return {
            "reports": reports,
            "timeline": timeline,
            "narrative": narrative,
            "alerts": alerts
        }