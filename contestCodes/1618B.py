for _ in range(int(input())):
    n = int(input())
    l = []
    s = input().split()
    l.append(s[0][0])
    k = 0
    # print(s)
    for i in range(n - 3):
        l.append(s[i][1])
        if s[i][1] != s[i + 1][0]:
            k = 1
            l.append(s[i + 1][0])

        # print(l)
    l.append(s[n-3][1])
    if k == 0:
        l.append('a')
    a = ''.join(l)
    print(a)