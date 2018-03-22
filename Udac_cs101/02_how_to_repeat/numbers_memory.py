
KiloByte = 8*2.0**10
MegaByte = 8*2.0**20
GigaByte = 8*2.0**30
TeraByte = 8*2.0**40

# Write Python code to print out how far light travels 
# in the units
# defined below.  

speed_of_light = 299792458      # meters per second
nano_per_sec = 1000000000.      #1 Billion
nanosecond = 1.0/nano_per_sec   # one billionth of a second
meter = 100                     # one meter is 100 centimeters
# d = v*t
nanodistance = speed_of_light / nano_per_sec
print "In a nanosecond the light travels ", nanodistance, "[m]"
# 1 second in km
# d = speed_of_light [m] * 1 s * 1 km
#                     s         1000 m
print "In 1 second => " , speed_of_light/1000. ," [km]"
print "In 0.4 ns => " , meter * speed_of_light *.4/nano_per_sec ,"[cm]"
print "In 12 ns => " , speed_of_light *12/nano_per_sec, "[m]"
print "In 7 ms => " , 7*speed_of_light/1000000. ," [km]"


# Cost per bit
# 1 TB    -   $100 USD
# 1  b    -    x

# On othe hand:
# 1 USD   -   1000000000.      #1 Billion nanoUSD
# x USD   -   y
print "The cost per bit in a TeraByte HD is nano$", 100.0*10.0**9/TeraByte , "USD"

print 10**9
print 10**12
print 10.0**9/10**12
print 100*10.0**9/10**12
print TeraByte
