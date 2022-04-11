for _ in range(int(input())):
    n = int(input())
    dictionary = {}
    l = list(map(int, input().split()))
    for i in l:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    # print(l)
    ans = 0
    for i, j in dictionary.items():
        if j > 1:
            if i == 0:
                ans += 1

            else:
                if -i in dictionary:
                    ans += 1
                    # print("yessss")
                else:
                    ans += 2

        else:
            ans += 1

    # print(dictionary)
    print(ans)