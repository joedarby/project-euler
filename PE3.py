
"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

num = 600851475143
x = 2

n = num

while n != 1:
    if n%x == 0:
        if n/x == 1:
        	print "The lowest prime factor of %s is %s" % (num, n)
        	break
        else:
        	n = n/x
    else:
        x += 1
    