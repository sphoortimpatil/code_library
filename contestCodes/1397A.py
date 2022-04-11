for _ in range(int(input())):
    n = int(input())
    s = ""
    for i in range(n):
        s = s + input()
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    k = 0
    for i,j in d.items():
        if j % n == 0:
            k = 1

        else:
            k = 0
            break
    if k == 1:
        print("Yes")
    else:
        print("No")