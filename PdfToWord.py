from pdf2docx import Converter
pdf_file = 'uma.pdf'
docx_file= 'uma.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()