"""

 Created by akiselev on 2019-05-31
 
 
"""

from itertools import groupby
groups = []
for k,g in groupby(input()):
    groups.append(list(g))      # Store group iterator as a list
l=[]
for i in groups:
    l.append("({}, {})".format(len(i),i[0]))
print(*l)
#print(*[(len(list(g)), int(k)) for k, g in groupby(input())])