"""

 Created by akiselev on 2019-06-02
 
 
"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command=list(input().split())
    com=command[0]
    if com=="discard":
        s.discard(int(command[1]))
    elif com=="remove":
        s.remove(int(command[1]))
    else:
        s.pop()
    #eval('s.{0}({1})'.format(*input().split()+['']))
print (sum(s))