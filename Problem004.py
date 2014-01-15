"""
@author: eshim

Date: 12/23/13
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def findLargestPalindrome():
	"""Finds the largest palindrome made from the product of two 3-digit numbers."""
	largestPalindrome = 0
	for i in range(999, 9, -1):
		for j in range(999, 99, -1):
			currentProduct = i * j
			if isPalindrome(currentProduct) and currentProduct > largestPalindrome :
				largestPalindrome = currentProduct
	return largestPalindrome


def isPalindrome(inputInt):
	"""Checks if the given value is a palindrome. Version 1"""
	# allocates memory for more values
	inputString = str(inputInt) # turn into iterable
	topIndex = len(inputString) - 1
	botIndex = 0

	while topIndex >= botIndex:
		if inputString[botIndex] == inputString[topIndex]:
			topIndex -= 1
			botIndex += 1
		else:
			return False

	return True

def isPalindrome(inputInt):
	"""Cheks if the given value is palindrome. Version 2"""
	inputString = str(inputInt) # turn into iterable

	return inputString == inputString[::-1]:


print findLargestPalindrome()
