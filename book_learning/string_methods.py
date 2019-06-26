#!/usr/bin/python -tt
# Source:
# LEARNING TO PROGRAM WITH PYTHON
# Richard L. Halterman
"""
Example: Using String Object Methods
"""


# Define a main() 
def main():
    a = "        ABCDEFGHIJKLMNOPQRSTUVWXYZ        "
    try:
        print("<<" + a + ">>")
        print("<<" + a.rstrip() + ">>")
        print("<<" + a.strip() + ">>")
    except:
        print("Error: ")


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
