"""

 Created by akiselev on 2019-05-16
 
 
"""

_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))