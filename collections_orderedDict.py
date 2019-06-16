"""

 Created by akiselev on 2019-05-30
 
 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
purchased = OrderedDict()
for _ in range(int(input())):
    name,space,price = input().rpartition(" ")
    if name in purchased:
        purchased[name]+=int(price)
    else:
        purchased[name]=int(price)
    #purchased[name] = purchased.get(name, 0) + int(price)
for i in purchased:
    print(i, purchased[i])
