"""

 Created by akiselev on 2019-05-19
 
 
"""

n=int(input())
pb={}
for i in range(n):
    name, phone = input().split()
    pb[name]=phone
#print (pb)
name=input()
while True:
    if name in pb.keys():
        print("{}={}".format(name, pb[name]))
    else:
        print("Not found")
    try:
        name=input()
    except EOFError:
        break