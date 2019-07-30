"""

 Created by akiselev on 2019-06-25
 
 start() & end()

These expressions return the indices of the start and end of the substring matched by the group.

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.

Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).
"""

import re
S = input()
k = "(?=({}))".format(input().strip())
matches = list(re.finditer(k, S))
if matches:
    print('\n'.join(str((m.start(1), m.end(1)-1)) for m in matches))
else:
    print('(-1, -1)')
