for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if a[i][j] == a[i + 1][j]:
                a[i][j] = a[i + 1][j]
    for i in range(m):
        print(a[i][k], end=' ')