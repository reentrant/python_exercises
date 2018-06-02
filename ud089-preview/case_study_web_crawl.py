#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Created on 20/05/2018
@author: jruiz
https://classroom.udacity.com/courses/ud1110
'''
import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/')
html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
print(soup.title)
# for link in soup.find_all('a'):
#     if link.get('title'):
#         print(link.get('href'))
for tag in soup.p.find_all('a'):
    print(tag)
print(soup.find(id="language"))


# Other example:
url = 'http://affirmyourlife.blogspot.com/2009/08/communication-affirmations.html'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
for br in soup.find_all('br'):
    print(br)
