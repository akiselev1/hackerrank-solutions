"""

 Created by akiselev on 2019-06-12
 
 Task

Perform append, pop, popleft and appendleft methods on an empty deque

.

Input Format

The first line contains an integer
, the number of operations.
The next

lines contains the space separated names of methods and their values.

Constraints

Output Format

Print the space separated elements of deque

.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2

"""
from collections import deque
N = int(input())
d = deque()
for i in range (N):
    op = input().split()
    if len(op) == 2:
        eval("d.{}({})".format(op[0],op[1]))
    else:
        eval("d.{}()".format(op[0]))
print (*d, sep=" ")