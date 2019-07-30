"""

 Created by akiselev on 2019-06-27
 
 Let's dive into the interesting topic of regular expressions!
 You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7,8 or 9.

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines.
Do not print the quotes.

"""
import re
def is_valid(num):
    if re.search(r'^[7-9][0-9]{9}$', num):
        return "YES"
    else:
        return "NO"


N = int(input())
for _ in range(N):
    l = input().strip()
    print(is_valid(l))