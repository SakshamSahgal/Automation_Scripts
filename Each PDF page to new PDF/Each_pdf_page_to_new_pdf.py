import os
import PyPDF2

# Open the PDF file
input_file = 'LTD Meerut PDF Queery,signed.pdf'
pdf_file = open(input_file, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Loop through each page and create a new PDF file for each page
for page in range(num_pages):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Add the current page to the PDF writer object
    pdf_writer.add_page(pdf_reader.pages[page])

    # Create a new PDF file name
    output_file = os.path.splitext(input_file)[0] + '_page%d.pdf' % (page+1)

    # Create a new PDF file and write the current page to it
    with open(output_file, 'wb') as output:
        pdf_writer.write(output)

# Close the PDF file
pdf_file.close()