### PDFs

import os
from pyPdf import PdfFileReader

path = "/Users/Fo/Dropbox/LearnPython/repo"

input_file_name = os.path.join(path, "PandP.pdf")

# PDFs have to be Read Binary
input_file = PdfFileReader(file(input_file_name, "rb"))

print "Pages: ", input_file.getNumPages()
print "Title:", input_file.getDocumentInfo().title

print input_file.getDocumentInfo()

# extract text from any given Pages

print input_file.getPage(0).extractText()

### Basic scraping

from urllib2 import urlopen

address = "https://realpython.com/practice/aphrodite.html"
page = urlopen(address)

# read everything on that page
text = page.read()

print text

# Find only stuff between a specific set of tags using indices 

start_tag = "<title>"
end_tag = "</title>"

start_index = text.find(start_tag) + len(start_tag)
end_index = text.find(end_tag)

print text[start_index:end_index]