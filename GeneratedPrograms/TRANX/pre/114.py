n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    a, b = map(int, input().split())
    a[a].append(b)
    a[b].append(b)
for i in range(n):
    a, b = map(int, input().split())
    a[a].append(b)
    a[b].append(b)
ans = 0
for i in range(1, n + 1):
    ans += abs(a[i] - a[i + 1])
print(ans)