for _ in range(int(input())):
    x, y = map(int, input().split())
    if (x + y) % 2 == 0:
        # if x % 2 == 0 and y % 2 == 0:
        #     print(x // 2, y // 2)
        # else:
        if x > y:
            x1 = (x - y) // 2
            y1 = y
        else:
            x1 = x
            y1 = (y - x) // 2
        print(x1, y1)
    else:
        print(-1, -1)