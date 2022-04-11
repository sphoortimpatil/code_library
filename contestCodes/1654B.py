mod = 10000000
for _ in range(int(input())):
    s = input()
    for i in range(1, len(s) ):
        # print(s[i+1::], i, s[i])
        if s[i] in s[i+1::]:
            continue
        else:
            s = s[i::]
            # print("ddddddd")
            break
    print(s)