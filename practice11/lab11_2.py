from PIL import Image
from pathlib import Path

folder = Path("images3")

for file in folder.iterdir():

    if file.suffix.lower() in [".jpg", ".png"]:

        image = Image.open(file)

        print(f"\nФайл: {file.name}")
        print(f"Width: {image.size}")
        print(f"Format: {image.format}")
        print(f"Color: {image.mode}")

        image.show()