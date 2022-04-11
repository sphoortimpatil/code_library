for _ in range(int(input())):
    n = int(input())
    k = 0
    a = []
    for i in range(1, n + 1):
        c = i * i * i
        s = i * i
        if s <= n:
            a.append(s)
        if c <= n:
            a.append(c)
        if c > n and s > n:
            break
        # print(a)
    print(len(set(a)))