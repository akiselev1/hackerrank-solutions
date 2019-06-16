"""

 Created by akiselev on 2019-05-29
 
 
"""

words={}
for _ in range(int(input())):
    a=input()
    if a in words:
        words[a]+=1
    else:
        words[a]=1
print(len(words))
print(*words.values(),sep=" ")