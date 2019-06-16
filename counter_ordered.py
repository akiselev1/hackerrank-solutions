"""

 Created by akiselev on 2019-06-12
 
 Input Format

A single line of input containing the string

.

Constraints

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde

Sample Output 0

b 3
a 2
c 2

Explanation 0

Here, b occurs times. It is printed first.
Both a and c occur times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.
"""

from collections import Counter
for each in Counter(sorted(input())).most_common(3):
    print(*each)


"""
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]


if __name__ == '__main__':
    s = list(input().strip())
    #print(s)
    s=sorted(s, key = s.count, reverse = True)
    #print(s)
    for _ in range(3):
        print("{} {}".format(s[0], s.count(s[0])))
        for item in range(s.count(s[0])):
            s.remove(s[0])
        #print(s)

"""