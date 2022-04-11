mod = 10000000
for _ in range(int(input())):
    s = input()
    z = s.count('0')
    o = s.count('1')

    print(min((len(s) - 1) // 2, o, z))