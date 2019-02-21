n, m, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    a[b].append(b)
    a[b].append(b)
for i in range(m):
    a, b = map(int, input().split())
    a[b].append(b)
    a[b].append(b)
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i][j] and a[i][j] == a[i][j]:
            a[i][j] = a[i + 1][j]
for i in range(n):
    print(a[i][])