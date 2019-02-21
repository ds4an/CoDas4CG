n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i][j] and a[i][j] == a[i + 1][j]:
            print(a[i][j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i + 1][
                j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i +
                1][j], a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i + 1][j],
                a[i + 1][j], a[i + 1][j], a[i + 1][j], a[i + 1][j])