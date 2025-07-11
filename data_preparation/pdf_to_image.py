import fitz  
import os

# Paths
pdf_folder = "/Users/laxmandongre/Downloads/REV_DATA_top_right_corner"
output_folder = "/Users/laxmandongre/Downloads/REV_DATA_top_right_corner_images"
zoom_x = 2.0  
zoom_y = 2.0  

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        pdf_name = os.path.splitext(filename)[0]
        doc = fitz.open(pdf_path)

        print(f"Processing {filename}...")

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=mat, colorspace=fitz.csRGB)

            image_filename = f"{pdf_name}_page_{page_number + 1}.jpg"  
            image_path = os.path.join(output_folder, image_filename)
            pix.save(image_path)

        doc.close()
