mod = 10000000
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = list(zip(a, b))
    # sorted(ab)
    # print(ab)
    ab.sort()
    # print(ab)
    for a, b in ab:
        if a <= k:
            k += b
    print(k)