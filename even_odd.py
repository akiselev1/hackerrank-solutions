"""

 Created by akiselev on 2019-05-16
 
 
"""

for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])

#pro level:
#for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])