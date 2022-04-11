for _ in range(int(input())):
    s = input()
    d = { }
    c = 0
    f = 0
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    # print(d)
    for i, j in d.items():
        if j > 1:
            c += 1
        elif j == 1 :
            f+=1
    c += f//2
    print(c)