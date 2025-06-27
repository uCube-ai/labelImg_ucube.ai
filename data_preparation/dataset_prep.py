
import os
import shutil
import random
from pathlib import Path

SOURCE_PARENT_DIR = "/Users/laxmandongre/Downloads/individual_folders"
DEST_DIR = "/Users/laxmandongre/Downloads/dataset_created"


# 🔢 Dataset split counts
NUM_TRAIN = 134
NUM_VAL = 7
NUM_TEST = 7

def collect_image_label_pairs(source_dir):
    image_extensions = ['.jpg', '.jpeg', '.png']
    image_label_pairs = []

    for subfolder in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, subfolder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                ext = Path(file).suffix.lower()
                if ext in image_extensions:
                    label_path = os.path.splitext(file_path)[0] + ".txt"
                    if os.path.exists(label_path):
                        image_label_pairs.append((file_path, label_path))
    return image_label_pairs

def split_dataset(pairs, num_train, num_val, num_test):
    random.shuffle(pairs)
    total_needed = num_train + num_val + num_test
    if len(pairs) < total_needed:
        raise ValueError(f"Not enough image-label pairs. Required: {total_needed}, Found: {len(pairs)}")

    return (
        pairs[:num_train],
        pairs[num_train:num_train + num_val],
        pairs[num_train + num_val:num_train + num_val + num_test]
    )

def copy_dataset(pairs, image_out_dir, label_out_dir):
    os.makedirs(image_out_dir, exist_ok=True)
    os.makedirs(label_out_dir, exist_ok=True)

    for img, label in pairs:
        shutil.copy(img, os.path.join(image_out_dir, os.path.basename(img)))
        shutil.copy(label, os.path.join(label_out_dir, os.path.basename(label)))

def organize_dataset():
    all_pairs = collect_image_label_pairs(SOURCE_PARENT_DIR)
    train, val, test = split_dataset(all_pairs, NUM_TRAIN, NUM_VAL, NUM_TEST)

    print(f"Total pairs found: {len(all_pairs)}")
    print(f"→ Train: {len(train)}\n→ Val: {len(val)}\n→ Test: {len(test)}")

    copy_dataset(train, os.path.join(DEST_DIR, "images/train"), os.path.join(DEST_DIR, "labels/train"))
    copy_dataset(val, os.path.join(DEST_DIR, "images/val"), os.path.join(DEST_DIR, "labels/val"))
    copy_dataset(test, os.path.join(DEST_DIR, "images/test"), os.path.join(DEST_DIR, "labels/test"))

    print("✅ Done organizing the dataset!")

if __name__ == "__main__":
    organize_dataset()
