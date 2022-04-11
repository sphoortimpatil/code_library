mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if a[i] > c + i + 1:
            c = (a[i] - i - 1 )
            # print(i,c)
    print(c)