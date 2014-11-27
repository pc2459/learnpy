from urllib2 import urlopen
import re

url = "https://realpython.com/practice/dionysus.html"
page = urlopen(url)
text = page.read()

print text

start_name = "Name: "
end_name = "</h2>"

name_start_index = text.find(start_name) + len(start_name)
name_end_index = text.find(end_name)

print text[name_start_index:name_end_index]

start_color = "Favorite Color: "
end_color = "</center>"

color_start_index = text.find(start_color) + len(start_color)
color_end_index = text.find(end_color)

print text[color_start_index:color_end_index]

## More elegant way:

for tag in ["Name: ", "Favorite Color: "]:
	start_tag = text.find(tag) + len(tag)
	end_tag = text[start_tag:].find("<")

	print text[start_tag:end_tag+start_tag].strip("\n")

# using RE - search for a tag, anything after, then a newline
# or an opening tag

for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
	match_results = re.search(tag, text)
	results = match_results.group()
	#sub out anything before the colon
	results = re.sub(".*:","",results)
	results = results.strip(" \n<")

	print results


