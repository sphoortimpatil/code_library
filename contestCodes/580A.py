mod = 10000000

n = int(input())
a = list(map(int, input().split()))
c1 = 1
c = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        # print(i + 1)
        c += 1
    else:

        c = max(c, c1)
        c1 = c
        c = 1
print(max(c, c1))