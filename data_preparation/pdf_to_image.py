import fitz  # PyMuPDF
import os

# Paths
pdf_folder = "/Users/laxmandongre/Downloads/Shop Dwg Sample/shop_rev_A"
output_folder = "/Users/laxmandongre/Downloads/Shop Dwg Sample/pdf_2_images_shop_drwg_pdf/rev_A"
zoom_x = 2.0  # Horizontal zoom (2.0 = 200% resolution)
zoom_y = 2.0  # Vertical zoom

os.makedirs(output_folder, exist_ok=True)

# Loop through PDFs
for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        pdf_name = os.path.splitext(filename)[0]
        doc = fitz.open(pdf_path)

        print(f"Processing {filename}...")

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            mat = fitz.Matrix(zoom_x, zoom_y)  # Control resolution
            pix = page.get_pixmap(matrix=mat, colorspace=fitz.csRGB)

            image_filename = f"{pdf_name}_page_{page_number + 1}.png"
            image_path = os.path.join(output_folder, image_filename)
            pix.save(image_path)

        doc.close()

