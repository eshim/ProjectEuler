"""
@author: eshim

Date: 12/23/13
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def findLargestPrimeFactor(inputInt):
	"""Finds the largest prime factor for the given input. """
	largestPrimeFactor = 0
	possibleFactor = 2
	maxValue = inputInt

	while maxValue / possibleFactor >= 1:
		if maxValue % possibleFactor == 0 and isPrime(possibleFactor):
			largestPrimeFactor = possibleFactor
			maxValue /= possibleFactor # if divisible
		possibleFactor +=1

	if largestPrimeFactor == 0: # if largest prime factor doesn't change
		return -1 

	return largestPrimeFactor


def isPrime(inputInt):
	"""Checks if the given input is prime."""
	# More value checking could be done, but covers my bases.
	if inputInt < 2: # Smallest prime is 2
		return False

	elif inputInt == 2: 
		return True

	for value in range(2, inputInt):
		if inputInt % value == 0:
			return False

	return True



print findLargestPrimeFactor(600851475143)
# 6857