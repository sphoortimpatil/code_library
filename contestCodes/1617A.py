for _ in range(int(input())):
    s = (input())
    s1 = sorted(s)
    a = s1.count('a')
    b = s1.count('b')
    c = s1.count('c')

    t = input()
    # print(a, b, c)
    # print(s)
    if t != 'abc' or a==0 or b==0 or c==0:
        # print("hhhhhhhhhhhh")
        print(''.join(s1))
    else:
        for i in range(a,a+c):
            # print(i)
            s1[i] = 'c'
        for i in range(a+c,a+b+c):
            # print(i)
            s1[i] = 'b'
        print(''.join(s1))