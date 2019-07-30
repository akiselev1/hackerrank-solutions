"""

 Created by akiselev on 2019-06-25
 

Given a list of rational numbers,find their product.

Concept
The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to
right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
>>> reduce(lambda x, y : x + y,[1,2,3])
6


Input Format

First line contains n , the number of rational numbers.
The next n lines contain two integers each, the numerator( ) and denominator( ) of the rational number in the list.

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest
form, i.e. numerator and denominator have no common divisor other than 1.

"""

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y : x*y, fracs)  # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)