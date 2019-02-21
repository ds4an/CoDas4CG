n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(1, n):
    if a[i] == a[i - 1]:
        ans += 1
print(ans)
