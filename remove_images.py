import fitz  # PyMuPDF

def remove_images_from_pdf(input_pdf_path, output_pdf_path):
    # Open the PDF file
    document = fitz.open(input_pdf_path)
    
    # Iterate through each page
    for page_num in range(1,len(document)):
        page = document[page_num]
        
        # Get the list of image dictionaries on the current page
        images = page.get_images(full=True)
        # Iterate through each image
        for image in images[:]:
            xref = image[0]  # xref is the reference number of the object
            print(page, image)
            document._deleteObject(xref)  # Delete the image object
    
    # Save the modified PDF to a new file
    document.save(output_pdf_path, garbage=3, deflate=True)
    document.close()

# Example usage:
input_pdf_path = 'CV_Javier_EN.pdf'
output_pdf_path = 'CV_Javier_EN_lite.pdf'
remove_images_from_pdf(input_pdf_path, output_pdf_path)

input_pdf_path = 'CV_Javier_ES.pdf'
output_pdf_path = 'CV_Javier_ES_lite.pdf'
remove_images_from_pdf(input_pdf_path, output_pdf_path)