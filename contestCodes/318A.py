mod = 10000000

n, k = map(int, input().split())
o = []
e = []
for i in range(1, n + 1):
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
l = o + e
print(l[k - 1])