"""

 Created by akiselev on 2019-06-11
 
 n Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'

Input Format

The first line contains the space separated values of
and .
The second line contains the polynomial

.

Output Format

Print True if

. Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1

Sample Output

True

"""
#Python 2
x,k = map(int, raw_input().split())
print k == input()