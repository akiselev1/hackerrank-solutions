"""

 Created by akiselev on 2019-06-26

The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Task

You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or

Both && and || should have a space " " on both sides.


 Sample Input

11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

"""

import re

for _ in range(int(input())):
    l = input()
    l = re.sub(r" &&(?= )", " and", l)
    l = re.sub(r" \|\|(?= )", " or", l)
    print(l)