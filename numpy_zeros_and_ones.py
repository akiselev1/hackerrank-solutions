"""

 Created by akiselev on 2019-07-18
 
 zeros

The zeros tool returns a new array with a given shape and type filled with

's.

import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]]

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]

ones

The ones tool returns a new array with a given shape and type filled with

's.

import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]]

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]

Task

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Output Format

First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.
"""

import numpy
d = tuple(map(int, input().split()))
print (numpy.zeros(d, dtype = numpy.int))
print (numpy.ones(d, dtype = numpy.int))