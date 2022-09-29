from PyPDF2 import PdfMerger
import glob



pdfs = sorted(glob.glob("opencv/*.pdf") )

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("opencv-book.pdf")
merger.close()
