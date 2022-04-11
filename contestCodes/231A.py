n = int(input())
p = 0
for _ in range(n):
    a = list(map(int,input().split()))
    if a[0] == 1 and a[1] == 1 or a[0] == 1 and a[2] == 1 or a[1] == 1 and a[2] == 1:
        p += 1
print(p)