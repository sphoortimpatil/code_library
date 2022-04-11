for _ in range(int(input())):
    input()
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    fx, fy = map(int, input().split())
    s = abs(ax-bx) + abs(ay-by)
    if ax == bx == fx and min(ay, by) < fy < max(ay, by) or ay == by == fy and min(ax, bx) < fx < max(ax, bx) :
        s += 2
    print(s)