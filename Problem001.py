"""
@author: eshim

Date: 12/23/13
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def findMultiplesSum(inputInt):
	"""Function to find the sum of multiples of 3 or 5 below the given int"""
	multiplesList = []
	for value in range(inputInt):
		if value % 3 == 0 or value % 5 == 0:
			multiplesList.append(value)

	return sum(multiplesList)

print findMultiplesSum(1000)
# 233168