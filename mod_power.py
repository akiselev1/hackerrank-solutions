"""

 Created by akiselev on 2019-06-17
 
Task
You are given three integers: a, b, and m , respectively. Print two lines.
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

Input Format
The first line contains a
, the second line contains b, and the third line contains m.
"""
a,b,m = [int(input()) for _ in '123']
print(pow(a,b),pow(a,b,m),sep='\n')
#print('{0}\n{1}'.format(pow(a,b), pow(a,b,m)))
