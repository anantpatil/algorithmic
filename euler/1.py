#!/usr/bin/env python

sum=0
for i in range(8192):
    if ((i % 3) == 0) or ((i % 5) == 0):
	sum = sum + i
    else:
	pass

print "Sum = " + str(sum)
