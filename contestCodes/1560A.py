l = [0]
i = 0
j = 1
while j !=1001:
    if i % 3 != 0:
      s = str(i)
      if s[-1] != '3':
        l.append(i)
        j+=1
    i +=1
#print(l)
for _ in range(int(input())):
    k = int(input())
    print(l[k])