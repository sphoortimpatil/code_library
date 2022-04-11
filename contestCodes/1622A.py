import math

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    d, e = 0, 0

    if a == b + c or b == a + c or c == b + a:
        print("Yes")
    else:
        if a == b:
            d = math.floor(c / 2)
            e = c - d
        elif b == c:
            d = math.floor(a / 2)
            e = a - d
            a = c
            # print(a, b, d, e)
        elif c == a:
            d = math.floor(b / 2)
            e = b - d
            b = c
            # print(a,b,d,e)

        if a + d == b + e:
            print("YES")
        else:
            print("No")