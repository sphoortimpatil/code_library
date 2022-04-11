mod = 10000000

n = int(input())
a = list(map(int, input().split()))
c = 0
a = sorted(a)
s1 = 0
# print(a)

while s1 <= sum(a):
    s1 += a.pop()
    c += 1
    # print(i+1)

print(c)