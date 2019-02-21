n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i + 1][j]:
            a[i][j] = 1
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i + 1][j]:
            print(a[i][j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i + 1][
                j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i +
                1][j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i + 1][j])