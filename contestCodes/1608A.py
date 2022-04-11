import math
l = []
i = 2
while len(l) < 1000:
    isprime = True
    h = int(math.sqrt(i)) + 1
    for j in range(2, h):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        l.append(i)
    i+=1
# print(len(l))

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        print(l[i],end=" " )
    print(end="\n")