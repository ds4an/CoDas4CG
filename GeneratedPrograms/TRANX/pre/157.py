for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        print(a[i][j], end=' ')
    print()