n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])
for i in range(n):
    x, y = map(int, input().split())
    a[x].append(y)
