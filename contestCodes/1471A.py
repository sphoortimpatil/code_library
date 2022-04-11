import math

for _ in range(int(input())):
    n, x = map(int, input().split())
    b = list(map(int, input().split()))
    mini = math.ceil(sum(b) / x)
    maxi = 0
    for i in range(n):
        maxi += math.ceil(b[i] / x )
    print(mini, maxi)