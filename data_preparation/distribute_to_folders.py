import os
import random
import shutil
from math import ceil

# Paths
image_folder = "/Users/laxmandongre/Downloads/Shop Dwg Sample/pdf_2_images/data_for_annotation"
output_base = "/Users/laxmandongre/Downloads/Shop Dwg Sample/pdf_2_images/individual_folders"
num_folders = 6

# Create output folders
for i in range(1, num_folders + 1):
    folder_path = os.path.join(output_base, f"folder_{i}")
    os.makedirs(folder_path, exist_ok=True)

# Get all image files
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
random.shuffle(image_files)  # Shuffle for random distribution

# Split and move files
images_per_folder = ceil(len(image_files) / num_folders)

for i in range(num_folders):
    folder_name = f"folder_{i+1}"
    start_index = i * images_per_folder
    end_index = start_index + images_per_folder
    for image_file in image_files[start_index:end_index]:
        src_path = os.path.join(image_folder, image_file)
        dst_path = os.path.join(output_base, folder_name, image_file)
        shutil.copy2(src_path, dst_path)  # Use move() if you want to delete original

print(f"✅ Distributed {len(image_files)} images into {num_folders} folders.")
