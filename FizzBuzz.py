"""

 Created by akiselev on 2019-06-21
 
 
"""
#!/usr/bin/python


for num in range(1,21):
	string=""
	if num % 3 == 0:
		string += "fizz"
	if num % 5 == 0:
		string += "buzz"
	if (num % 3 != 0) and (num % 5 != 0) :
		string = str(num)
	print (string)