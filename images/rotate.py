from PIL import Image
from pathlib import Path

# Path to the images folder
image_folder = Path(".")

# Supported image formats
extensions = [".jpg", ".jpeg", ".png", ".webp", ".gif"]

for img_path in image_folder.iterdir():
    if img_path.suffix.lower() in extensions:
        with Image.open(img_path) as img:
            rotated = img.rotate(90, expand=True)  # 90° counter-clockwise
            rotated.save(img_path)
        print(f"Rotated {img_path.name}")
