# -*- coding: utf-8 -*-
'''
@author: jruiz
'''
# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

def add_to_index(my_index,keyword,url):
    for key, links in my_index:
        if keyword == key:
            if url not in links:
                links.append(url)
            return
    my_index.append([keyword, [url]])
    return

def add_page_to_index(my_index,url,content):
    for keyword in content.split():
        add_to_index(my_index, keyword, url)

if __name__ == '__main__':
    index = []
    add_page_to_index(index,'fake.text',"This is a test")
    print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]