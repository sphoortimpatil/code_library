for _ in range(int(input())):
    s = list(map(int, input().split()))
    a = {max(s[0],s[1]),max(s[2],s[3])}
    s = sorted(s)
    b = {s[2],s[3]}
    if a == b:
        print("YES")
    else:
        print("NO")