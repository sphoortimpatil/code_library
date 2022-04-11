n, q = map(int, input().split())
s = input()
s1 = [0]
c = 0
for i in s:
    c += ord(i)-96
    s1.append(c)
#print(s1)
for i in range(q):
    l, r = map(int, input().split())
    print(s1[r] - s1[l-1])