t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if a[i][j] == a[i][j]:
                a[i][j] = a[i][j]
    for i in range(n):
        for j in range(n):
            if a[i][j] == a[i][j] and a[i][j] == a[i][j]:
                a[i][j] = a[i][j]
    for i in range(n):
        for j in range(n):
            if a[i][j] == a[i][j]:
                a[i][j] = a[i][j]
    for  in :