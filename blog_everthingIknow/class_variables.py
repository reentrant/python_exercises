#!/usr/bin/python -tt

class Party:
    x = 5

    def __init__(self):
        self.x += 1
        print(self.x)

a = Party()
b = Party()