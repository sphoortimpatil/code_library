for _ in range(int(input())):
    n = (input())
    a = list(n)
    n = int(n)
    c = 0
    if n % 2 == 0:
        print(0)
    elif int(a[0]) % 2 == 0:
        print(1)
    else:
        for i in range(len(a)):
            # print(int(a[i]))
            if int(a[i]) % 2 ==0:
                c += 1
                break
        if c != 0:
            print(2)
        else:
            print(-1)