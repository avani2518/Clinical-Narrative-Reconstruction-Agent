import os

from src.ner.entity_extractor import EntityExtractor

extractor = EntityExtractor()

folder = "data/raw"

for filename in os.listdir(folder):

    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    result = extractor.extract(text)

    print("\n" + "=" * 50)
    print(filename)
    print("=" * 50)

    print(result)