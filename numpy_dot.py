"""

 Created by akiselev on 2019-07-23
 
 dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11

cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2

Task

You are given two arrays A and B. Both have dimensions of N X N.
Your task is to compute their matrix product.
"""

import numpy
n = int(input())
A = numpy.array([input().split() for _ in range(n)], int)
B = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(A, B))