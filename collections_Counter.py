"""

 Created by akiselev on 2019-05-17
 
 
"""

from collections import Counter
nshoes=int(input())
shoe_sizes=list(map(int, input().split()))
ncustomers=int(input())
inv=Counter(shoe_sizes)
sum=0
for i in range(ncustomers):
    size,price=map(int, input().split())
    if inv[size]:
        sum += price
        inv[size] -= 1

print(sum)
