
def gcd(a,b):
	while (b>0):
		print b
		t = b
		b = a % b
		a = t
		print a		
	return a
	
gcd(28,35)
