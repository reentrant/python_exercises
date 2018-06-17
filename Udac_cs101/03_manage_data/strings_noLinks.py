
# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(start_page):
    start_link = start_page.find('<a href=')

    #Insert your code below here
    if -1 == start_link:
        return (None,0)
    start_quote = start_page.find('"', start_link)
    end_quote = start_page.find('"', start_quote + 1)
    url = start_page[start_quote + 1:end_quote]
    return url, end_quote


start_page =' <a href="www.mypage.com">my web<a>'
print get_next_target(start_page)
