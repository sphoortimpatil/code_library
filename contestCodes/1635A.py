mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s = s | a[i]
    print(s)