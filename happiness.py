"""

 Created by akiselev on 2019-05-29
 
 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
h=0
for i in range(n):
    if arr[i] in A:
        h+=1
    if arr[i] in B:
        h-=1
print(h)

#print (sum((i in A) - (i in B) for i in arr))
