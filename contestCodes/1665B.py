mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = len(set(a))
    c = 0
    m = {}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    l = max(m.values())
    # print(m.values(),"val")
    # print(l,"l")
    if l == n:
        print(0)
        continue
    else:

        k = n - l
        # print("l", l, k)
        while k > 0:
            if l > k:
                c += k + 1
            else:
                c += l + 1
            # print((n - l), c)
            k -= l
            l = l * 2

            # print("ul", l, k)
        
        print(c)