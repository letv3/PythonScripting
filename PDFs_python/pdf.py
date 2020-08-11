from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdfs):
    '''method to combine all pdfs in one'''

    merger = PdfFileMerger()
    for file in pdfs:
        print(file)
        merger.append(file)
    merger.write('super.pdf')
    return merger

pdf_combiner(inputs)
# with open('dummy.pdf', 'rb') as file:
#     reader = PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
#
#     print(reader.numPages)



