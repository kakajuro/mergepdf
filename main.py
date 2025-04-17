import sys
import pymupdf as pdf

doc = pdf.open()

args = sys.argv
pdfs = []

for arg in args:
	if ".pdf" in arg:
		pdfs.append(arg)

for path in range(len(pdfs)):
	src = pdf.open(pdfs[path])
	doc.insert_pdf(src)
	print(f"Added pdf {path+1} of {len(pdfs)}")
	src.close()

res = input("Output file name: ")

if ".pdf" not in res:
	res += ".pdf"

doc.save(res)
