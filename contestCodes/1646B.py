mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s_r = 0
    ss = sum(a)
    s_b = ss - s_r
    k = 0
    f = 0

    for i in range(n):
        s_r += a[i]
        s_b = ss - s_r
        k += 1
        if k < n - k and s_r > s_b:
            f = 1
            break
    if f == 1:
        print("YES")
    else:
        print("NO")