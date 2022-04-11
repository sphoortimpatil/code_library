for _ in range(int(input())):
    n, l, r, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    # print(a)
    c = 0
    for i in a:
        if i > r or k - i < 0:
            break
        if i >= l and i <= r:
            k -= i
            # print(i,k)
            c += 1
    print(c)