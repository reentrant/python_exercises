'''
@author: jruiz
'''
# The current index includes a url in the list of urls
# for a keyword multiple times if the keyword appears
# on that start_page more than once.

# It might be better to only include the same url
# once in the url list for a keyword, even if it appears
# many times.

# Modify add_to_index so that a given url is only
# included once in the url list for a keyword,
# no matter how many times that keyword appears.

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:
                entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return '''<html> <body> This is a test start_page for learning to crawl!
<p> It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">
learn to crawl</a> before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body>
</html>'''

        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
</body> </html>'''

        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '''<html> <body> I cant get enough
<a href="http://www.udacity.com/cs101x/index.html">crawling</a></body></html>'''

        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '''<html>
<body>The magic words are Squeamish Ossifrage!</body></html>'''
    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(start_page):
    start_link = start_page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = start_page.find('"', start_link)
    end_quote = start_page.find('"', start_quote + 1)
    url = start_page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(start_page):
    links = []
    while True:
        url, endpos = get_next_target(start_page)
        if url:
            links.append(url)
            start_page = start_page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        start_page = tocrawl.pop()
        if start_page not in crawled:
            content = get_page(start_page)
            add_page_to_index(index, start_page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(start_page)
    return index

def add_page_to_index(index, url, content):
    splitlist = [' ', '<html>', '<body>', '<p>']
    words = split_string(content, splitlist)
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None



def split_string(source,splitlist):
    word_list = []
    new_word = ''
    #print source.split()
    for c in source:
        if c in splitlist:
            if new_word:
                word_list.append(new_word)
                new_word = ''
        else:
            new_word += c
    if new_word:
        word_list.append(new_word)
    return word_list


if __name__ == '__main__':
    index = crawl_web("http://www.udacity.com/cs101x/index.html")
    print lookup(index,"is")
#>>> ['http://www.udacity.com/cs101x/index.html']
    for word, links_list in index:
        print len(links_list), "\t", word, "\t", links_list