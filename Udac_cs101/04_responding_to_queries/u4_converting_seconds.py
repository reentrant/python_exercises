# -*- coding: utf-8 -*-

# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(secs):
  h = 0
  m = minutes = 0
  s = 0
  s = secs % 60
  if (s == 1):
    s__str = '1 second'
  else:
    s__str = str(s) + ' seconds'
    
  minutes = int(secs / 60)
  m = minutes % 60
  
  if (m == 1):
    m__str = '1 minute, '
  else:
    m__str = str(m) + ' minutes, '
    
  
  if (minutes >= 60):
    h = minutes / 60
  
  if (h == 1):
    h__str = '1 hour, '
  else:
    h__str = str(h) + ' hours, '
  
  time = h__str + m__str + s__str
  return time
    
    

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds