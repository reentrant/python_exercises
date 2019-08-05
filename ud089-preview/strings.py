'''
Created on 13/05/2018
'''


def string(headlines):
    '''
    # set news_ticker to a string that contains no more than 140
    characters long.
    # HINT: modify the headlines list to verify your loop works with 
    different inputs
    '''
    news_ticker = ""
    length = 0
    for headline in headlines:
        for c in headline:
            if length <= 140:
                news_ticker += c
                length += 1
            else:
                break
        if length <= 140:
            news_ticker += '\n'
            length += 1
            print(length)
        else:
            break
    return news_ticker


some_headlines = ["Local Bear Eaten by Man",
                  "Legislature Announces New Laws",
                  "Peasant Discovers Violence Inherent in System",
                  "Cat Rescues Fireman Stuck in Tree",
                  "Brave Knight Runs Away",
                  "Papperbok Review: Totally Triffic"]


if __name__ == '__main__':
    try:
        print(string(some_headlines))
    except:
        print("What???")
