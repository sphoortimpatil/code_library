mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m1 = max(a)
    m2 = max(b)
    if m1 > m2:
        for i in range(n):
            if b[i] > a[i]:
                a[i], b[i] = b[i], a[i]
    else:
        for i in range(n):
            if a[i] > b[i]:
                b[i], a[i] = a[i], b[i]
    print(max(a)*max(b))