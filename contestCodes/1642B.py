mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    c = 0
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
            c += 1
    m = max(d.values())
    for i in range(c):
        print(c, end=" ")
    for i in range(n - c):
        c += 1
        print(c, end=" ")
    print()