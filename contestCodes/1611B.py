for _ in range(int(input())):
    a, b = map(int, input().split())
    l = min(a, b)
    a1, a2 = l, (a + b) // 4

    print(min(a1, a2))