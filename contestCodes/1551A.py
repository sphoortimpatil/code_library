import math

for _ in range(int(input())):
    n = int(input())
    a = math.floor(n/3)
    # print(a)
    if n % 3 == 0:
        print(a,a)
    elif (n % 3 ) % 2 == 0:
        print(a,a+1)
    else:
        print(a+1,a)