"""

 Created by akiselev on 2019-06-11

>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>>
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]

 
 The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5

Input Format

The first line contains
and separated by a space.
The next

lines contains the space separated marks obtained by students in a particular subject.

Constraints


Output Format

Print the averages of all students on separate lines.

The averages must be correct up to

decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

"""
n,x = map(int, input().split())
l = []
for i in range (x):
    l.append(map(float,input().split()))

for i in (zip (*l)):
    print (sum(i)/x)