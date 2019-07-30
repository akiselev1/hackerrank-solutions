"""

 Created by akiselev on 2019-06-21
 
 
"""

#!/usr/bin/env python3

#recursive
def F(x):
	if (x == 1) or (x == 0):
		return 1
	else:
		return (F(x-1) + F(x-2))


#program

a = int (input ("Enter the number N for Fibonacci sequence: "))
print (F(a))
