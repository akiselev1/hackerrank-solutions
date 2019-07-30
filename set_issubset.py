"""

 Created by akiselev on 2019-06-20
 

You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

"""
T = int(input())
for i in range(T):
    #x, a, z, b = input(), set(input().split()), input(), set(input().split())
    _, A = input(), set(input().split())
    _, B = input(), set(input().split())
    print(A.issubset(B))
    #if A.intersection(B) == A:
    #    print("True")
    #else:
    #    print("False")