n = int(input())
for _ in range(n):
    s = (input())
    l = len(s) - 2
    if l + 2 > 10:
        k = s[0] + str(l) + s[-1]
        print(k)
    else:
        print(s)