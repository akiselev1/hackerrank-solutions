"""

 Created by akiselev on 2019-05-17
 
 
"""

from itertools import permutations
#s,n = input().split()
s = "HACK"
n = 2
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')