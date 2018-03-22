
mixed_up = ['apple',3,'oranges',27,
[1,2,['alpha','betha']]]

print mixed_up

beatles = [['John',1940], ['Paul',1942],
	['George',1943],['Ringo',1940]]
print beatles	
print beatles[3][0]

# Given the variable countries defined as:
#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the array.

print countries[1]
print countries[1][1]

# What multiple of Romania's population is the population
# of China? Please print your result.

result = countries[0][2]/countries[2][2]
print str(result)

## How to print a more precise answer?
