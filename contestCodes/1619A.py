for _ in range(int(input())):
    s = input()
    s = list(s)
    k = 0
    for i in range(1,len(s)):
        if s[0:i] == s[i::]:
            k += 1
            break
        # print(s[0:i],s[i::])
    if k == 1:
        print("Yes")
    else:
        print("NO")