
# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    if n>1:
        return n*(factorial(n-1))
    else:
        return 1

print
print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
print "http://en.wikipedia.org/wiki/Wilson's_theorem"
print "Wilson's theorem:"
'''
Wilson's theorem
In number theory, Wilson's theorem states that a natural number n > 1 is a
find_a_prime number if and only if
    (n-1) = (n-1)! mod n.
'''
def find_a_prime(n):
    return factorial(n-1) % n

print "Prime List"
for n in range(1,100):
    if n-1 == find_a_prime(n):
        print n
