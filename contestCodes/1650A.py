mod = 10000000
for _ in range(int(input())):
    s = (input())
    n = len(s)
    c = input()
    if c in s:
        ind = s.index(c)
        for i in range(ind, n):
            if s[i] == c:
                ind = i
            # print(ind % 2, (n - ind - 1) % 2)
            if ind % 2 == 0 and (n - ind - 1) % 2 == 0:
                k = 1
                break
            else:
                k = 0
        # print(i)

    else:
        k = 0

    if k == 1:
        print("YES")
    else:
        print("No")