"""

 Created by akiselev on 2019-06-11
 
 Your task is to sort the string

in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

"""
lower = []
upper = []
digits_odd = []
digits_even=[]
for i in input().strip():
    if i.isupper():
        upper.append(i)
    if i.islower():
        lower.append(i)
    if i.isdigit():
        if int(i) % 2 ==0:
            digits_even.append(i)
        else:
            digits_odd.append(i)
print("".join(sorted(lower)+sorted(upper)+sorted(digits_odd)+sorted(digits_even)))



'''
Pythonic solutions:

print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
'''