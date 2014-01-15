"""
@author: eshim

Date: 12/23/13
Problem 4:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Copied from: 
http://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers

I don't think I could have done it better
"""

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b: 
     
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b / gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)


print lcmm(*range(1,21))  
# 232792560