"""


The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the 
square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.

"""

myList = range(1, 101)


def squareSum(n):
	"""Using sum of squares algorithm or brute force list comprehension. Works for int or list of ints"""
	try:
		return n * (n + 1) * (2*n + 1) / 6
	except TypeError:
		return sum([x*x for x in n])


def sumSquare(n):
	"""Using squared sum algorithm or brute force list comprehension. Works for int or list of ints."""
	try:
		return n*n * (n + 1)*(n + 1) / 4
	except TypeError:
		total = sum(n)
	 	return (total * total)


print sumSquare(myList) - squareSum(myList)
