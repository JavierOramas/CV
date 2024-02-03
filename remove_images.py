import sys
from os import PyPDF2

if len(sys.argv) != 3:
    print("Usage: python script_name.py input_pdf output_pdf")
    sys.exit(1)

input_pdf = sys.argv[1]
output_pdf = sys.argv[2]

with open(input_pdf, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        pdf_writer.addPage(page)

    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)
