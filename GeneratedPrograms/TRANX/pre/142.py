n, m = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i + 1][j]:
            a[i][j] = a[i + 1][j]
print(len(a))