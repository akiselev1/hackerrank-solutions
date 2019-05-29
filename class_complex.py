"""

 Created by akiselev on 2019-05-24
 
 
"""
import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.imaginary * no.real + self.real * no.imaginary)

    def __truediv__(self, no):
        re = (self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        im = (self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        return Complex(re, im)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        return '{0:.2f}{1:+.2f}i'.format(self.real, self.imaginary + 0)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')