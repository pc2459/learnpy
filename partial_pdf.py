"""
Programme that extracts pages from a PDF within a given range 
using GUI elements
"""

from easygui import *
from pyPdf import PdfFileWriter, PdfFileReader

#let user choose file using fileopenbox

input_filename = fileopenbox("","Select a PDF to extract from...","*.pdf")

# choose beginning page using enterbox

startpage = enterbox("Beginning of extract range:", "")

# check if valid; use msgbox if invalid

if startpage.isdigit() == False or int(startpage) <= 0:
	msgbox("Your beginning page was invalid; try again")
	startpage = enterbox("Beginning of extract range:", "")

# choose end page using enterbox

endpage = enterbox("End of extract range:", "")

# check if valid; use msgbox if invalid

if endpage.isdigit() == False or int(endpage) <= int(startpage):
	msgbox("Your end page was invalid; try again")
	endpage = enterbox("Beginning of extract range:", "")


# choose output file using savefilebox

# check if is same as input; use msgbox to alert if sorted

# output new file