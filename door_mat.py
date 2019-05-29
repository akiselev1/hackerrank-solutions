"""

 Created by akiselev on 2019-05-14
 
 
"""
#n, m = map(int,input().split())
n,m = 7, 21
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))