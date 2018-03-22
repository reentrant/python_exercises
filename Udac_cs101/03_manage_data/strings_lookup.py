
string = "aaaa"
search = 'a'
ix =0
while True:
	last = string.find(search,ix)
	print "ix = " + str(ix)

	if  last >-1:
		ix = last+1
	else:
		last = ix
		print "last = " + str(last)
		break


	
