"""

 Created by akiselev on 2019-06-20
 
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the n sets.

Print True, if A is a strict superset of each of the n sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
"""
A = set(input().split())
print(all(A > set(input().split()) for _ in range(int(input()))))
#n = int(input())
#ans = "True"
#for i in range(n):
#    B = set(input().split())
#    if not(A.issuperset(B) and len(A) > len(B)):
 #       ans = "False"
#print(ans)