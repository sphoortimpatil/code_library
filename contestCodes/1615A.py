for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    # l = min(a)
    # c = 0
    # for i in  range(n):
    #     if a[i] > l:
    #         c += a[i] - l
    #         a[i] = l
    # print(a)
    # print(c)
    # l = 1 + (c/n)
    # h = l + 1
    s = sum(a)
    if s % n == 0:
        print(0)
    else:
        print(1)