

'''
How far travels the ligth for this time?

d = v * t

'''
light_speed = 300000 # km/s

def distance(time):
	return light_speed*time

# Latency times 

print distance(1)	# light_bulb_latency = 1 #(seconds)
print distance(0.4e-9)	# cpu_register_latency = 0.4 # ns
print distance(12e-9) 	# DRAM_latency	     = 12  # ns
print distance(7e-3)	# HD_latency	     = 7   # ms

'''
The cost per bit in a 2gb dram...
2G n$10e9 
1b n$? = 10e9 / (2 ** 30 * 2 * 8) #How many bits are in 2Gb?

The cost per bit in a 1T HD...
1T n$100e9
1b ?

'''
print 100e9 / ( 2 ** 40 * 8 ) 
