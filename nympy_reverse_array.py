"""

 Created by akiselev on 2019-06-11
 
 
"""

import numpy

def arrays(arr):
    return (numpy.array(arr[::-1], float))
arr = input().strip().split(' ')
result = arrays(arr)
print(result)