#!/usr/bin/env python

import math

"""
Generator for prime numbers.
"""

def nextprime():
    primes = [2, 3]
    yield primes[0]
    yield primes[1]
    while True:
	n = search_next_prime(primes)
	primes.append(n)
	yield n

def search_next_prime(l):
    # next prime is going to be at least next add number
    # to the last one in list
    n = l[-1] + 2
    lim = math.sqrt(n)
    while True:
	for m in l:
	    if m > lim:
		return n
	    if (n % m) == 0:
		break;
	n = n + 2

np=nextprime()
#print type(np)
for i in range(1638400):
    print np.next()
