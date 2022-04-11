for _ in range(int(input())):
    n, m, rb, cb, rd, cd = map(int, input().split())
    t1 = rd-rb
    t2 = cd-cb
    if rb > rd:
        t1 = (n-rb) + (n-rd)
    if cb > cd:
        t2 = (m-cb)+(m-cd)
    print(min(t1,t2))