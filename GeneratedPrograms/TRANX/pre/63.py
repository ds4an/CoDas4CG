n, n = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    print(a[i][i], end=' ')
for i in range(n):
    print(a[i][i], end=' ')