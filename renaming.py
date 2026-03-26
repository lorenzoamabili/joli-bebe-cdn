import os

folder_path = r"C:\dev\joli-bebe-cdn\estivo"

for filename in os.listdir(folder_path):
    if filename.startswith("IMG_"):
        new_name = filename.replace("IMG_", "", 1)

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
    if filename.startswith("_MG_"):
        new_name = filename.replace("_MG_", "", 1)

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
