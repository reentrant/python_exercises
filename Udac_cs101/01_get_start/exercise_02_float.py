
# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the variables
# defined below.    

speed_of_light = 299792458   # meters per second
meter = 100                  # one meter is 100 centimeters
nanosecond = 1.0/1000000000  # one billionth of a second

new_units_cm_per_ns = speed_of_light * meter * nanosecond
print new_units_cm_per_ns 