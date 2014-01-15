"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""
from math import sqrt

def whichPrime(n):
	
	if n == 1:
		return 2
	

	elif n > 1:
		primeList = []
		curr_val = 3 
		iterator = 1
		while iterator < n:
			
			# don't bother checking any even numbers
			primeTest = True
			for prime in primeList:#[value for value in primeList if value <= sqrt(curr_val)]:
				if prime > sqrt(curr_val):
					# if it iterates to this point, it's a prime
					break
				elif curr_val % prime == 0:
					primeTest = False
					break

			if primeTest:

				primeList.append(curr_val)
				iterator += 1
			curr_val += 2


		return primeList.pop()

print whichPrime(100010)

# print range(100)
