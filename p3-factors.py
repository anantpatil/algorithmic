#!/usr/bin/env python

"""
Find the largest prime factor of a given number.

Algo: Starting with 2, divide with prime numbers ranging till sqrt(num)
till the remainder is 1. The last prime number which divided
successfully (remiander 0) is the largest prime number.

n <- given num
m <- largest prime num
m = 2
while n > 1
    do
	r = n % m
	if r is 0
	    n = n / m
	else
	    m = next_prime()

return m

To find next_prime, we keep a list of all consecutive prime numbers we
have ben trying to divide the number. Idea is to try next potential
number by dividing it with the available list of primes.

next_prime(l)
    // l is list of tried primes
    m = last elem of l + 2
    while m is divisible by any prime num from 2 to sqrt(m) from l
	m += 2

    return m

"""
import math

tried=[] # list of tried prime nums
factors=[]
def prime_factors(x):
    tried.append(2)
    r = x % 2
    if r == 0:
	factors.append(2)
	while r == 0 and x > 1:
	    x = x / 2
	    r = x % 2
    if x <= 1:
	return factors

    lim = int(math.sqrt(x))
    n = 3
    tried.append(3)
    while x > 1:
	r = x % n
	if r == 0:
	    factors.append(n)
	    x = x / n
	else:
	    n = nextprime(tried, lim)
	    if n == -1:
		break # done
	    tried.append(n)
	    #print "trying next prime " + str(n)

    if len(factors) == 0:
	# No factors found, its a prime number
	return [x]
    else:
	return factors

def nextprime(l, lim):
    n = l[-1] + 2
    # from the list l don't try with 2 as all the protential numbers are
    # odd.
    while divisibleby(n, l[1:]) and n <= lim:
	n += 2 # 2 is the only prime even num

    if n > lim:
	return -1
	
    return n

def divisibleby(n, s):
    # brute force check to see if number is prime
    lim = int(math.sqrt(n))
    for i in s:
	if i > lim:
	    break;
	if n % i == 0:
	    return True

    return False

def isprime(n):
    lim = int(math.sqrt(n))
    for i in range(2, lim):
	if n % i == 0:
	    print "Divisible by: " + str(i)
	    return False

    return True

#s=prime_factors(600851475143)
s=prime_factors(29)
#s=prime_factors(6008514751439)
#s=prime_factors(13195)
#s=prime_factors(131959)
#s=prime_factors(46908737)
print "All prime factors: " + str(s)
print "Largest prime factor: " + str(s[-1])
print "Number of primes tried: " + str(len(tried))
