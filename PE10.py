"""Objective: Find the sum of all prime numbers less
than 2 million.
"""

import time


def sieve(n):
	t0 = time.time()

	not_prime = set()
	prime_sum = 0
	
	for i in range(2, int(n**0.5)+1):
		if i not in not_prime:
			for j in range(i**2, n+1, i):
				if j not in not_prime:
					not_prime.add(j)

	for i in range(2,n):
		if i not in not_prime:
			prime_sum += i

	print prime_sum
	print "This took", time.time() - t0, "seconds"


sieve(2000000)
