"""

 Created by akiselev on 2019-06-04
 
 
"""
def isPrime(num):
    if num == 1:
        return "Not prime"
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

T=int(input().strip())
for i in range(T):
    possiblePrime=int(input().strip())
    print(isPrime(possiblePrime))