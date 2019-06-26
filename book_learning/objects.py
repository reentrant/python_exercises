#!/usr/bin/python -tt
# Source:
# LEARNING TO PROGRAM WITH PYTHON
# Richard L. Halterman
"""
Example: Using  Objects 
"""

class Rational:
    """
    Represent a fraction
    """
    def __init__(self, num, den):
        self.__numerator = num
        if den != 0:
            self.__denominator = den
        else:
            raise ValueError("Division by Zero")


# Define a main() 
def main():
    try:
        f1 = Rational(1, 2)
        print(isinstance(f1, Rational))
        print(isinstance(f1, object))
        f2 = Rational(0, 0)
        print(f1.__numerator)
    except Exception as e:
        print(e)
        print("Error: Using the dot operator with mangled names...")
        

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
