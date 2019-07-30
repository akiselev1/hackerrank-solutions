"""

 Created by akiselev on 2019-06-17
 
 
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
#a = int(input())
#b = int(input())
#print(a//b)
#print(a%b)
#print(divmod(a,b))

print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))