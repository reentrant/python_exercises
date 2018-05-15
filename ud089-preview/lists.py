'''
Created on 12/05/2018

@author: jruiz
'''

names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']

#===============================================================================
# This code has NO effect!!!
#===============================================================================
for name in names:
    name = name.title()
print(names)
#===============================================================================
# How to modify a list
#===============================================================================
for i in range(len(names)):
    names[i] = names[i].title()
print(names)
#===============================================================================
# Avoid mutable default arguments:
#===============================================================================
def todo_list(new_task, base_list=['wake up']):
    """
    The list object base_list is only created once: when the todo_list function 
    is defined. Lists are mutable objects. This list object is used every time 
    the function is called, it isn't redefined each time the function is called.
     Because todo_list appends an item to the list, base_list can get longer 
     each time that todo_list is called.
    """
    base_list.append(new_task)
    return base_list

print(todo_list("check the mail"))
#['wake up', 'check the mail']
print(todo_list("begin orbital transfer"))
#['wake up', 'check the mail', 'begin orbital transfer']
#===============================================================================
# Create an HTML List
#===============================================================================
#define the  html_list function
def html_list(list_of_strings):
    html = "<ul>\n"
    for e in  list_of_strings:
        html = html + "<li>"  + e + "</li>\n"
    html += "</ul>"
    return html

print(html_list(['First element', 'Second element', 'Third element']))
# <ul>
# <li>First element</li>
# <li>Second element</li>
# <li>Third element</li>
# </ul>
