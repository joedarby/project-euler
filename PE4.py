"""Problem:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""Solution:
Find the product of every number in (100,998)*(100,998) and convert to a string. If the string is 6 digits long, check if the reverse 
of the string is equal to the string itself. If it is, the number is a palindrome. Add this to a list of palindromic numbers and
find the maximum of this list at the end.

"""


palindromes = []

for i in range(998,100,-1):
	for j in range(998,100,-1):
		num = i * j
		string = str(num)
		if len(string) == 6:
			if string == string[::-1]:
				palindromes.append(string)

print max(palindromes)

