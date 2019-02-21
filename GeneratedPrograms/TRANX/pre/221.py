n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans += 1
print(ans)