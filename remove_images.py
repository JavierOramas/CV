import PyPDF2

input_pdf = "your_document.pdf"
output_pdf = "your_document_no_images.pdf"

with open(input_pdf, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        pdf_writer.addPage(page)

    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)
