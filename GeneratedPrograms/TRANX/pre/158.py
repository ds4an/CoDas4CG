n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == '_STR:1_':
            ans += 1
print(ans)