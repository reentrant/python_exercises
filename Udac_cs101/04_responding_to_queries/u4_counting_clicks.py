'''
@author: jruiz
'''
# 2 Gold Stars
# One way search engines rank pages
# is to count the number of times a
# searcher clicks on a returned link.
# This indicates that the person doing
# the query thought this was a useful
# link for the query, so it should be
# higher in the rankings next time.

# (In Unit 6, we will look at a different
# way of ranking pages that does not depend
# on user clicks.)

# Modify the index such that for each url in a
# list for a keyword, there is also a number
# that counts the number of times a user
# clicks on that link for this keyword.

# The result of lookup(index,keyword) should
# now be a list of url entries, where each url
# entry is a list of a url and a number
# indicating the number of times that url
# was clicked for this query keyword.

# You should define a new procedure to simulate
# user clicks for a given link:

# record_user_click(index,word,url)

# that modifies the entry in the index for
# the input word by increasing the count associated
# with the url by 1.

# You also will have to modify add_to_index
# in order to correctly create the new data
# structure, and to prevent the repetition of
# entries as in homework 4-5.


def record_user_click(index, keyword, url):
    links_list = lookup(index, keyword)
    for entry in links_list:
        if url == entry[0]:
            entry[1] = entry[1] + 1
            return
    print "ERROR: Bad input"


def add_to_index(index, keyword, url):
    clicks = 0
    for key, links_list in index:
        if key == keyword:
            for entry in links_list:
                if url == entry[0]:
                    return
            links_list.append([url, clicks])
    # not found, add new keyword to index
    index.append([keyword, [[url, clicks]]])

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
#     for entry in index:
#         if entry[0] == keyword:
#             return entry[1]
    for word, links_list in index:
        if word == keyword:
#             print len(links_list), "\t", word, "\t"
            return links_list
    return None


if __name__ == '__main__':
    #Here is an example showing a sequence of interactions:
    index = crawl_web('http://www.udacity.com/cs101x/index.html')
    print lookup(index, 'good')
#     print lookup(index, 'is')
#     for word, links_list in index:
#         print len(links_list), "\t", word, "\t", links_list
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 0]]
    record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
    print lookup(index, 'good')
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 1]]
