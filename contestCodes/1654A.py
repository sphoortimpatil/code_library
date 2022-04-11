mod = 10000000
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a1 = a
    m_1 = max(a)
    a1.remove(m_1)
    m_2 = max(a1)
    print(m_1+m_2)