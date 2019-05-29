"""

 Created by akiselev on 2019-05-16
 
 
"""

def merge_the_tools(string, k):
    # your code goes here
    if len(string)<2:
        print(string)
        return
    n=len(string)
    for i in range(0,n,k):
        res=[]
        substring=string[i:i+k]
        for j in substring:
            if j not in res:
                res.append(j)
        print(''.join(res))
    return

if __name__ == '__main__':
    #string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)