'''
Created on 08/01/2018
@author: jruiz
'''

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()

    except:
        return "error"

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed): 
    tocrawl = [seed] 
    crawled = [] 
    index = {}
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

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url) 
        return
    # not found, add new keyword to index 
    index[keyword] = [url] 

def lookup(index, keyword): 
    for entry in index: 
        if entry[0] == keyword: 
            return entry[1] 
    return None

def print_all_links(web_links):
    for e in web_links:
        print e

links = get_all_links(get_page("http://www.nytimes.com/pages/todayspaper/index.html"))
print_all_links(links)
print_all_links(crawl_web("https://www.nytimes.com/membercenter/sitehelp.html"))