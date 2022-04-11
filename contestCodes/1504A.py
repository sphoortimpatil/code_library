n = int(input())
for _ in range(n):
    s = input()
    s = "a" + s
    #print(s)
    if s == s[::-1]:
        s = s[1:] + "a"
        #print(s[0:-1])
    if s == s[::-1]:
        print("No")
    else:
        print("Yes")
        print(s)