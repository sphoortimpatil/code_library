for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(set(a))
    # print(l)
    k = a.count(l[0])
    f = a.count(l[1])
    if k > f:
        print(a.index(l[1])+1)
    else:
        print(a.index(l[0])+1)
    # if a[1] != f and a[2] == a[1]:
    #     print(1)
    # elif a[1] != f and a[2] != a[1]:
    #     print(2)
    # else:
    #     for i in range(1, n):
    #         if a[i] != f:
    #             print(i+1)
    #             break