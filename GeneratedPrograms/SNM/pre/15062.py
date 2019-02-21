n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += a[i] - a[i]
print(ans)
