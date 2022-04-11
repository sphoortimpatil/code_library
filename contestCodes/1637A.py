mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sorted(a)
    if s == a:
        print("NO")
    else:
        print("YES")
    # k = 0
    # for i in range(1,n - 1):
    #     l1 = sorted(a[0:i])
    #     l2 = sorted(a[i::])
    #     l3 = l1 + l2
    #     print(l1, l2, l3)
    #     if l3 != s:
    #         print(l3,i)
    #         k = 1
    #         break
    #
    # if k == 1:
    #     print("Yes")
    # else:
    #     print("No")