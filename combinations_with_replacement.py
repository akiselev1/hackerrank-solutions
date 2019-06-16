"""

 Created by akiselev on 2019-05-31
 
 
"""
from itertools import combinations_with_replacement

s, k = input().split()

for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))