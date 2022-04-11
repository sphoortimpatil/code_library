t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    j = 0
    dup_s = [s[0]]
    for i in range (1,n):
        if s[i] != dup_s[j]:
            dup_s.append(s[i])
            j += 1
    #print(dup_s)
    k = len(dup_s)
    l = len(set(dup_s))

    if k == l:
        print("Yes")
    else:
        print("No")