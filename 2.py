#!/usr/bin/env python

from itertools import takewhile

"""
Find the sum of all even fibonacci numbers below 4M.
Using generators.
"""
def fibonacci():
    a, b = 0, 1
    while True:
	yield a
	a, b = b, a+b

fib=fibonacci()
#print [n for n in takewhile(lambda x: x < 400, fib)]
total=sum([n for n in takewhile(lambda x: x < 4000000, fib)])
print total
