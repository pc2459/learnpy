### GUI using easygui

from easygui import *

# msgbox("This is the message!","This is the title!","This is the button")

choices = ("Blue","Yellow","???")
buttonbox("What is your favourite colour?","Pick...",choices)

from pyPdf import PdfFileReader, PdfFileWriter

input_filename = fileopenbox("","Select a PDF...", "*.pdf")

if input_filename is None: # exit on cancel
	exit()

rotations = (90,180,270)
message = "Rotate the PDF by how many degrees?"
degrees = buttonbox(message,"Choose rotation...",rotations)

# let user choose output file

output_filename = filesavebox("","Save the PDF as...","*.pdf")

while input_filename == output_filename:
	msgbox("Can't overwrite the original!","Please choose another file!")
	output_filename = filesavebox("","Save the PDF as...","*.pdf")
if output_filename is None:
	exit()

# read and rotate

input_file = PdfFileReader(file(input_filename,"rb"))
output_PDF = PdfFileWriter()

for page_num in range(0, input_file.getNumPages()):
	page = input_file.getPage(page_num)
	page = page.rotateClockwise(int(degrees))
	output_PDF.addPage(page)

output_file = file(output_filename, "wb")
output_PDF.write(output_file)
output_file.close()
