for _ in range(int(input())):
    sumList = list(map(int,input().split()))
    setSumList = list(set(sumList))
    a = []
    l = min(sumList)
    a1 = sumList[0]
    a2 = sumList[1]
    a3 = sumList[6] - a1 -a2
    print(a1,a2,a3)