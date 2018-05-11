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
			raise None


# Define a main() 
def main():

	try:
		f1 = Rational(1, 2)
		print(f1.__numerator)
		
	except:
		print("Error: Using the dot operator with mangled names...")
		

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
