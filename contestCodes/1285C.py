import math

x = int(input())
X = math.floor(math.sqrt(x))
ans = 1
for i in range(X,0,-1):
    if x % i == 0 and math.gcd(i, x//i) == 1:
        print(i, x//i)
        break