import sys
import os.path
import pymupdf as pdf

doc = pdf.open()

args = sys.argv
pdfs = []

res = sys.argv[-1]

for arg in range(len(args)):
	if arg == 0:
		continue

	if ".pdf" not in args[arg]:
		print("All arguments must be pdf files.")		
		sys.exit(1)
	else:
		if os.path.isfile(args[arg]):
			pdfs.append(args[arg])
		elif arg == len(args) - 1:
			pass
		else:
			print(f"{args[arg]} does not exist.")
			sys.exit(1)

for path in range(len(pdfs)):
	src = pdf.open(pdfs[path])
	doc.insert_pdf(src)
	print(f"Added pdf {path+1} of {len(pdfs)}")
	src.close()


doc.save(res)
print(f"{pdfs[-1]} created sucessfully.")