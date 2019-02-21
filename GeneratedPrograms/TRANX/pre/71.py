n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    a, b = map(int, input().split())
    a[a].append(b)
    a[b].append(b)
for i in range(n):
    print(a[i][0], a[i][1])
for i in range(n):
    print(a[i][0], a[i][1])