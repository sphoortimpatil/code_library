for _ in range(int(input())):
    n, k = map(int, input().split())
    s = (list(map(int, input().split())))
    #print(s)
    d = {}
    d1 = []
    j = 1
    for i in s:
        if i not in d:
            d[i] = 1
            j = 1
            d1.append(j)
            j += 1
        else:
            d[i] += 1
            #print(d[i])
            j = d.get(i,0)
            if j > k:
                d1.append(0)
            else:
                d1.append(j)
            j += 1

    # print(d)
    print(*d1)