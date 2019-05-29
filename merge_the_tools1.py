"""

 Created by akiselev on 2019-05-16
 
 
"""

#S, N = input(), int(input())
S, N = "AABCAAADA", 3
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))