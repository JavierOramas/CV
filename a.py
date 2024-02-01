import sys
import pdfkit

if len(sys.argv) != 3:
    print("Usage: python script_name.py input_pdf output_pdf")
    sys.exit(1)

input_pdf = sys.argv[1]
output_pdf = sys.argv[2]
import fitz  # PyMuPDF


# Function to check if a page object contains images
def page_contains_images(page):
    img_list = page.get_images(full=True)
    return len(img_list) > 0

# Open the input PDF
pdf_document = fitz.open(input_pdf)

# Create a new PDF document for the output
output_document = fitz.open()

# Iterate through the pages and add non-image pages to the output
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    if not page_contains_images(page):
        output_document.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

# Save the modified PDF
output_document.save(output_pdf)
output_document.close()

print("Images removed and saved to", output_pdf)
