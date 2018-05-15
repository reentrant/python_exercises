'''
Created on 11/05/2018

@author: jruiz
'''
def hours2days(hours):
    days = hours // 24
    hours = hours % 24
    return days, hours

print(hours2days(34))
# (1, 10)

colors = ["red", "yellow", "green"]
for tpl in enumerate(colors):
    print(tpl)
