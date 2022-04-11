mod = 10000000
for _ in range(int(input())):
    n = int(input())
    s = 10

    if n % 7 == 0:
        print(n)
    else:
        n1 = n - n % 7 + 7
        n2 = n - n % 7

        # print(k,c1,c2,"cccc")
        if n1 // s == n // s:
            print(n1)
        else:
            print(n2)