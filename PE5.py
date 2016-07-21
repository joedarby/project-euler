"""Problem:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""Solution:
To test a number is evenly divisible by all numbers 1 to n, it is sufficient to test a number is evenly divisible
by all numbers in the upper half of the range.
Starting from n*2, test for even divisbility. When a bad divisor is found, increment the test
number by n and start again.
When a number is reached which is divisible by all required numbers, break and print this number.
"""

import time

print """This program finds the smallest number divisible by all numbers from 1 
to a certain value."""

num = int(raw_input("What number to test up to?"))

t0 = time.time()

trial = 2 * num



divisors = []
for i in range(num/2 +1,num + 1):
		divisors.append(i)


count = len(divisors) -1
i = divisors[count]

print divisors

while count >= 0:
	i = divisors[count]
	if trial % i == 0:
		count -= 1
	else:
		trial += num
		count = len(divisors) -1


print "The smallest number evenly divisible by all numbers numbers 1 to %s is %s" % (num, trial)

print time.time() - t0


"""Currently very slow. Need to get rid of unnecessary use of list."