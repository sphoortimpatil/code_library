for _ in range(int(input())):
    a, b, c = map(int, input().split())
   # print(a,b,c)
    k = abs(a-b)
    if k == 1 or k*2 < c or a > (k *2) or b > (k *2) :
        print(-1)

    else:
        z = c + k
        if z >(k*2):
            z = z % (k*2)
        print(z)