n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    if a[i] == a[i]:
        ans += 1
print(ans)