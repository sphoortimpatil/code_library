for _ in range(int(input())):
    a, b = map(int, input().split())
    m = abs(a - b)
    if m == 0:
        print(0)
    if m % 2 == 0 and a > b or m % 2 != 0 and b > a:
        print(1)
    elif m % 2 == 0 and b > a or m % 2 != 0 and a > b:
        print(2)