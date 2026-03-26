import os
from PIL import Image

# Folders
input_folder = r"C:\dev\joli-bebe-cdn\estivo"
output_folder = "cdn_webp"

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Supported formats
extensions = (".jpg", ".jpeg")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(extensions):
        # Remove IMG_ prefix if present
        new_name = filename
        if new_name.startswith("IMG_"):
            new_name = new_name.replace("IMG_", "", 1)

        input_path = os.path.join(input_folder, filename)

        # Open image
        with Image.open(input_path) as img:
            # Rotate 90° left (counterclockwise)
            img = img.rotate(90, expand=True)

            # Convert to WebP
            base_name = os.path.splitext(new_name)[0]
            output_path = os.path.join(output_folder, f"{base_name}.webp")
            img.save(output_path, "WEBP", quality=80, optimize=True)

        print(f"Processed: {filename} → {base_name}.webp")
