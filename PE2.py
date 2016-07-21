"""
Each new term in the Fibonacci sequence is generated by 
adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find the sum 
of the even-valued terms.
"""

def find_fibs():
	"""Finds all Fibonacci numbers upto 4 million and puts 
	into a list
	"""
	i,j = 1,1
	fibs = [i,j]

	while i + j < 4000000:
		k = i + j
		fibs.append(k)
		i = j
		j = k
		continue

	return fibs

target = 0

for i in find_fibs():
	if i % 2 == 0:
		target += i
	else:
		target = target

for i in find_fibs(): print i
print "\nThe sum of the even Fibonacci numbers to the limit is", target







