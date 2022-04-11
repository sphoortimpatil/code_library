for _ in range(int(input())):
    k = list(input())
    s = list(input())
    # print(k)
    # print(s)
    a = [k.index(s[0])+1]
    d = 0
    for i in range(1,len(s)):
        ind = k.index(s[i])+1
        a.append(ind)
        d += abs(ind-a[i-1])
    print(d)