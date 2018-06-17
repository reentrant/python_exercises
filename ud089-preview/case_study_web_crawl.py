#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Created on 20/05/2018
@author: jruiz

Wikipedia Crawler
It starts at a random article.
Then it will look for a link in the first paragraph.
The crawling stops when the Philosophy article is found,
or maximum max_steps are reached,
or there is a cycle in the articles.
'''
import time
import urllib
import requests
from bs4 import BeautifulSoup




def continue_crawl(search_history, target_url, max_steps = 25):
    '''
    search_history is a list of strings which are the urls of Wikipedia articles. The last item in the list most recently found url.
    target_url is a string, the url of the article that the search should stop at if it is found.
    Example:
    continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],
                       'https://en.wikipedia.org/wiki/Philosophy')
                       
    continue_crawlshould return True or False following these rules:

    if the most recent article in the search_history is the target article the 
    search should stop and the function should return False.
    If the list is more than max_steps=25 urls long, the function should return 
    False.
    If the list has a cycle in it, the function should return False
    otherwise the search should continue and the function should return True.

    '''
    result = True
    if search_history[-1] == target_url:
        result = False
        print("Reached the target article!")
    elif search_history[-1] == None:
        result = False
        print("The first paragraph does not have a link")
    elif search_history[-1] in search_history[:-1]:
        result = False
        print("the list has a cycle in it:")
        print( search_history[-1] )
    elif len(search_history) > max_steps:
        result = False
        print("the list is more than max_steps urls long:")
        for link in search_history:
            print(link)
    else:
        print()    
    return result

def find_first_link(url):
    '''
    return the first link as a string, or return None if there is no link
    '''
    first_link = None
    #===========================================================================
    # download html of last article in article_chain
    #===========================================================================
    print(url)
    result = requests.get(url)
    result_html = result.text
    soup = BeautifulSoup(result_html, 'html.parser')
    print(soup.title.string)
    #===========================================================================
    # This div contains the article's body
    #===========================================================================
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            first_relative_link = element.find("a", recursive=False).get('href')
            # Build a full url from the relative article_link url
            first_link = urllib.parse.urljoin('https://en.wikipedia.org/',
                                              first_relative_link)
            break
    if not first_link:
        print(soup.find(id = 'mw-content-text').p.get_text())
    return first_link


#===============================================================================
# Startup page
#===============================================================================
start_page = 'https://en.wikipedia.org/wiki/Special:Random'
target_url = 'https://en.wikipedia.org/wiki/Philosophy'
article_chain = [start_page]
    
while continue_crawl(article_chain, target_url): 
    #===========================================================================
    # find the first link in that html
    #===========================================================================
    first_link = find_first_link(article_chain[-1])
    # add the first link to article_chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
    

