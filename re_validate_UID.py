"""

 Created by akiselev on 2019-06-17
 
ABCXYZ company has up to

employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 -9).
It should only contain alphanumeric characters (a-z,A-Z,0-9)
No character should repeat.
There must be exactly 10 characters in a valid UID.

Input Format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

"""
from collections import Counter
import re

def isvalid(uid):
    if len(uid) != 10:
        return False
    if not uid.isalnum():
        return False
    if set(i for i in uid if uid.count(i)>1):
        return False
    #numbers
    num=[i for i,j in Counter(uid).items() if i.isdigit()]
    if len(num)<3:
        return False
    #capitals
    caps=[i for i,j in Counter(uid).items() if i.isupper()]
    if len(caps)<2:
        return False
    return True

def is_valid(uid):
    uid = ''.join(sorted(uid))
    has_2_or_more_upper = bool(re.search(r'[A-Z]{2,}', uid))
    has_3_or_more_digits = bool(re.search(r'\d{3,}', uid))
    has_10_proper_elements = bool(re.search(r'^[a-zA-Z0-9]{10}$', uid))
    no_repeats = not bool(re.search(r'(.)\1', uid))

    if has_2_or_more_upper and has_3_or_more_digits and has_10_proper_elements and no_repeats:
        return True
    else:
        return False


T = int(input())
for _ in range(T):
    l = input().strip()
    if is_valid(l):
        print("Valid")
    else:
        print("Invalid")
