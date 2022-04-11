import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = len(str(n))-1
    b = 10 ** a
    k = 9
    if n < 10:
        print(n)
    else:
        k = 9 * a
        while n >= (a+1)*b:
            n = n - b
        x = n / (b/10)
        y,x = math.modf(x)
        y = int(y*10)
        if y >= x:
            k += x
        else:
            k += (x - 1)
        print(k)