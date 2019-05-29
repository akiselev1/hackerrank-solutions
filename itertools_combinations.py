"""

 Created by akiselev on 2019-05-25
 
 
"""
from itertools import combinations
s,k = input().split()
a=[]
for i in range(1,int(k)+1):
    a+=sorted(list(combinations(sorted(s),int(i))))
for i in a:
    print ("".join(i))