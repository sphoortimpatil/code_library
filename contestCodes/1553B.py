for _ in range(int(input())):
    s = input()
    t = input()
    lt = len(t)
    ls = len(s)
    f = 0
    for i in range(ls):
        if f:
            break
        for j in range(ls):
            k = lt-1-j
            if i + j <k:
                continue
            # print(i)
            # print(j)
            l1 = i
            r = i + j
            l2 = r - k
            # print(s[l1:r+1])
            # print(s[l2:r])
            # print(s[l2:r][::-1])
            # print(s[l1:r+1] + s[l2:r][::-1])
            if s[l1:r+1] + s[l2:r][::-1] == t:
                f = 1
                break
    if f:
        print("Yes")
    else:
        print("No")