
# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string start_page.

# start_page = contents of a web start_page
start_page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'
start_link = start_page.find('<a href=') # it returns an index

hiperlink = start_page[start_link:]
print hiperlink

url  = hiperlink[hiperlink.find('"')+1:hiperlink.find('"',hiperlink.find('"')+1)] # find from an index
print url
