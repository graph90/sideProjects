import PyPDF2

pdf_file = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

txt_file = open('example.txt', 'w')

for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text = page.extractText()
    txt_file.write(text)

pdf_file.close()
txt_file.close()
