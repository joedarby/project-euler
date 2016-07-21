"""
Problem:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Solution:
Test numbers for primaility by trial division by previously found primes. 
Add new primes to list.
When required number of primes is found, stop and print the last one.
"""

primes = [2]
num = 3

while len(primes) < 10001:
	count = 1
	while count < len(primes):
		for i in primes:
			if num % i != 0:
				count += 1
			else:
				num += 2 #move to next odd number
				count = 1
				break
	else:
		primes.append(num)

print primes[-1]


