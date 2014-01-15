"""
@author: eshim

Date: 12/23/13
Problem 2:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four 
million, find the sum of the even-valued terms.
"""

def findEvenFibonacciSumUpTo(inputInt):
	"""Iterate up to the given value"""
	evenFibonacciSum = 0
	firstValue, secondValue = 0, 1

	while secondValue < inputInt:

		if secondValue % 2 == 0:
			evenFibonacciSum += secondValue

		nextValue = firstValue + secondValue
		firstValue = secondValue
		secondValue = nextValue

	return evenFibonacciSum

		
 
print findEvenFibonacciSumUpTo(4000000)
# 4613732