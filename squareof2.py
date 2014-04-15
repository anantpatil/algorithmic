#!/usr/bin/env python2.7

"""
    Digit 7 is missing from all the powers of 2 starting from 72. This
    is true for numbers atleast till 10000.
"""
for i in xrange(1, 100):
    n = 2 ** i
    if '7' not in str(n):
	print i, n
