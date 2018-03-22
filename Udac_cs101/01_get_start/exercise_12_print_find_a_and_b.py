
#Assume text is a variable that
#holds a string. Write Python code
#that prints out the position
#of the second occurrence of 'zip'
#in text, or -1 if it does not occur
#at least twice.

#For example,
#   text = 'all zip files are zipped' -> 18
#   text = 'all zip files are compressed' -> -1

text = "all zip files are zipped" 
print text
#DO NOT USE IMPORT

#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

first = text.find("zip")# first occurrence
print  first
print text.find("zip",first+1) # find from an index
text = 'all zip files are compressed'
print text
first = text.find("zip")# first occurrence
print text.find("zip",first+1) # find from an index
