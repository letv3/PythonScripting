import PyPDF2
import sys




#open file

pdf_input = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))

watermark_pdf = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for page_num in range(pdf_input.getNumPages()):
    pdf_page = pdf_input.getPage(page_num)
    pdf_page.mergePage(watermark_pdf.getPage(0))
    output.addPage(pdf_page)

output.write(open('wtr_super.pdf', 'wb'))

# input_file.close()
# watermark_file.close()
# merged_file.close()
