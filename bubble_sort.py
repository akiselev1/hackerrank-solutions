"""

 Created by akiselev on 2019-05-30
 
 
"""

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
num_swaps=0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            num_swaps+=1
print("Array is sorted in {} swaps.".format(num_swaps))
print("First Element:",a[0])
print("Last Element:",a[-1])