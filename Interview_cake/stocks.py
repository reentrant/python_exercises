# -*- coding: utf-8 -*-
'''
Created on 27/02/2018

@author: jruiz
https://www.interviewcake.com/
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am 
local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the 
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock 
yesterday.

No "shorting"�you must buy before you sell. You may not buy and sell in the
 same time step (at least 1 minute must pass).
'''
from functools import reduce

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_today = [10]

def get_max_profit(prices_list):
    #===========================================================================
    # from any position what is the maximum value to the right?
    #===========================================================================
    profits = []
    i = 0
    while len(prices_list[i + 1:]) > 0:
#         print i, #index
#         print prices_list[i + 1:], # the sell_price options
        maximum = reduce(lambda a, b: a if (a > b) else b, prices_list[i + 1:])
        #=======================================================================
        # profit
        #=======================================================================
        profits.append(maximum - prices_list[i])
        i += 1
    if profits:
        return reduce(lambda a, b: a if (a > b) else b, profits)
    else:
        raise ValueError('Getting a profit requires at least 2 prices')

if __name__ == '__main__':
    print(get_max_profit(stock_prices_yesterday))
# Returns 6 (buying for $5 and selling for $11)
    print(get_max_profit(stock_prices_today))