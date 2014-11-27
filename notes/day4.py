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

# Using Regex to do the same, allowing for weirdness in the tags

import re

my_address = "https://realpython.com/practice/dionysus.html"

html_page = urlopen(my_address)
html_text = html_page.read()
# Python 3: html_text = html_page.read().decode('utf-8')

match_results = re.search("<title .*?>.*</title .*?>", html_text,
re.IGNORECASE)

# I'll note that this is still not perfect - what if there is a 
# space BEFORE the title tag, i.e. < title>?

title = match_results.group()
title = re.sub("<.*?>", "", title) # remove HTML tags

print title

### Beautiful Soup

from bs4 import BeautifulSoup

url2 = "https://realpython.com/practice/profiles.html"
profiles_page = urlopen(url2)
profiles_text = profiles_page.read()

print profiles_text

soup = BeautifulSoup(profiles_text)

# BS's get_text() function strips out HTML tags
print soup.get_text()

# get only hrefs of as 
# then get full texts of those hrefs
baseurl = "https://realpython.com/practice/"

a_list = soup.find_all("a")
for a in a_list:
	urlpage = urlopen(os.path.join(baseurl,a["href"]))
	urltext = urlpage.read()
	soup2 = BeautifulSoup(urltext)
	print soup2.get_text()



