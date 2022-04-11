mod = 10000000
for _ in range(int(input())):
    n = int(input())
    if n == 4:
        a = 1
        b = 1
        c = 1
        d = 1
    elif n == 5:
        a = 1
        b = 2
        c = 1
        d = 1
    elif n == 6:
        a = 3
        b = 1
        c = 1
        d = 1
    elif n % 2 == 0:
        a = 2
        c = 2
        d = 2
        b = n - (2 * 3)

    else:
        c = 2
        d = 1
        a = 2
        b = n - 5
    print(a, b, c, d)