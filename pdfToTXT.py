import PyPDF2

# open the PDF file in read-binary mode
pdf_file = open('example.pdf', 'rb')

# create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# create a text file for output
txt_file = open('example.txt', 'w')

# iterate over each page in the PDF file
for page_num in range(pdf_reader.numPages):
    # get the page object
    page = pdf_reader.getPage(page_num)

    # extract the text from the page
    text = page.extractText()

    # write the text to the text file
    txt_file.write(text)

# close the files
pdf_file.close()
txt_file.close()
