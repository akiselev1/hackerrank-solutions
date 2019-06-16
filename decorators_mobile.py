"""

 Created by akiselev on 2019-06-04
 
 
"""

def wrapper(f):
    def fun(l):
        # complete the function
        #print(l)
        #for i in range(len(l)):
        #    l[i] = "+91 {} {}".format(l[i][-10:-5],l[i][-5:])
        #fun = f(l)
        f("+91 "+num[-10:-5]+" "+num[-5:] for num in l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
