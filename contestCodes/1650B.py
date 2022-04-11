import math

mod = 10000000
for _ in range(int(input())):

    l, r, a = (map(int, input().split()))
    m = 0
    x = 0

    # # r = (l+r)//2
    # for i in range(l, (r + 1)):
    #     f = math.floor(i / a) + i % a
    #     print(i, f)
    #     m = max(m, f)
    # print(m)
    x = math.floor(r / a)
    # print(x * a <= r)
    a2 = (math.floor(r / a) + r % a)
    a1 = 0
    # a1 = (math.floor((x * a - 1) / a) + (x * a - 1) % a)
    if x * a <= r and x * a > l:
        a1 = (math.floor((x * a - 1) / a) + (x * a - 1) % a)
    # else:
    #     a2 = (math.floor(r / a) + r % a)
    print(max(a1, a2))