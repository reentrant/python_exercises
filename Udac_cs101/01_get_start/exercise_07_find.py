#Write Python code that initializes the variable 
#start_link to be the value of the position 
#where the first '<a href=' occurs in a start_page.

start_page = '<div id="top_bin">	<div id="top_content" class="width960">		<div class="udacity float-left">			<a href="/">'

start_link = start_page.find("<a href=")
print start_page
print start_link

