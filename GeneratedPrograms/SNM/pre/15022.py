n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(m):
    l, r = map(int, input().split())
    l.append(l)
