#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
"""
As a scripting language, Python has a large number of modules to help with a variety of tasks. This means that scripts can take advantage of existing functionality instead of writing lines of code from scratch. Modules that could be of interest for testers are
<a href="https://www.crummy.com/software/BeautifulSoup/" target="_blank">processing HTML</a>
or 
<a href="http://selenium-python.readthedocs.io/api.html" target="_blank">driving a web browser</a>

https://openpyxl.readthedocs.io/en/stable/
A Python library to read/write Excel 2010 xlsx/xlsm files
"""
from datetime import datetime

import pytz

utc = pytz.utc # utc is Coordinated Universal Time
ist = pytz.timezone('Asia/Kolkata') #IST is Indian Standard Time

now = datetime.now(tz=utc) # this is the current time in UTC
print(datetime.now())
ist_now = now.astimezone(ist) # this is the current time in IST.
print(ist_now)
print(pytz.country_timezones['mx'])
tzinfo = pytz.timezone('America/Monterrey')
print(now.astimezone(tzinfo))



