
import sys

url = ""

page = '<li><a href="http://www.nytimes.com/membercenter/sitehelp.html">Help</a></li>\
 </ul>\
 <div class="mainTabsContainer tabsContainer">\
 <ul id="mainTabs" class="mainTabs tabs">\
 <li class="first mainTabHome"><a href="http://www.nytimes.com">Home Page</a></li>\
 <li class="mainTabTodaysPaper"><a href="http://www.nytimes.com/pages/todayspaper/index.html">Today\'s Paper</a></li>\
 <li class="mainTabVideo"><a href="http://www.nytimes.com/video">Video</a></li>\
 <li class="mainTabMostPopular"><a href="http://www.nytimes.com/mostpopular">Most Popular</a></li>'

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if -1 == start_link:
        return (None,0)
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
#
def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
# >>>
# http://www.nytimes.com/membercenter/sitehelp.html
# http://www.nytimes.com
# http://www.nytimes.com/pages/todayspaper/index.html
# http://www.nytimes.com/video
# http://www.nytimes.com/mostpopular

# Define a main() function that prints a little greeting.
def main():
# Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'World'
    print 'Hello', name
    print "Script name: "+ sys.argv[0]

    print url
    print "len(page) = " + str(len(page))
# >>> len ('julian')
# 6

    print_all_links(page)
    sys.exit(0)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
#  Therefore, it's common to have the boilerplate if __name__ ==... shown above
# to call a main() function when the module is run directly,
# but not when the module is imported by some other module.