from src.pipeline import ClinicalPipeline

pipeline = ClinicalPipeline()

result = pipeline.process_folder("data/raw")

print("\n===== NARRATIVE =====\n")
print(result["narrative"])

print("\n===== ALERTS =====\n")

for alert in result["alerts"]:
    print(alert)