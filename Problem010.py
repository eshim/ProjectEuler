from math import sqrt

def sumPrimeUnder(n):
	if n < 2:
		return -1

	elif n == 2:
		return 2
	
	elif n > 2:
		primeList = []
		curr_val = 3 
		while curr_val < n:
			
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

			curr_val += 2

		primeList.insert(0, 2) # add the first prime back to the list
		# print primeList
		return sum(primeList)

print sumPrimeUnder(2000000)