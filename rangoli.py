"""

 Created by akiselev on 2019-05-14
 
 
"""
import string
alpha = string.ascii_lowercase
#The string module contains a set of useful constants, such as ascii_letters and digits, and the module is often still imported for that reason.

print(alpha)
#n = int(input())
n=4
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(s)
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print(L)
print('\n'.join(L[:0:-1]+L))