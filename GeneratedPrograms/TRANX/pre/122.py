n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    a[a - 1].append(b)
    d[b - 1].append(b)
for i in range(m):
    a, b = map(int, input().split())
    a[a].append(b)
    d[b].append(b)
for i in range(m):
    a, b = map(int, input().split())
    a[a].append(b)
    d[b].append(b)
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(b)
for i in range(m):
    a, b = map(int, input().split())
    d[a].()