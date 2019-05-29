"""

 Created by akiselev on 2019-05-23
 
 
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print (a//b)
    except Exception as myval:
        print ("Error Code:", myval)