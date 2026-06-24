import os

from src.ner.entity_extractor import EntityExtractor

extractor = EntityExtractor()

for filename in os.listdir("data/raw"):

    filepath = os.path.join("data/raw", filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    print("\n" + "="*50)
    print(filename)
    print("="*50)

    print(extractor.extract(text))