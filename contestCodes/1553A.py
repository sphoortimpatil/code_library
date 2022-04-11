import math

for _ in range(int(input())):
    n = int(input())
    x = math.floor(n/10)
    if  n % 10==9:
        print(x+1)
    else:
         print(x)