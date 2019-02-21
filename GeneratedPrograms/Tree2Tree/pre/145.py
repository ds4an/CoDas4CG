n = int(n[1])
a = list(map(int, input().split()))
for i in range(1, n + 1):
    ans += a[i] * a[i - 1]
for i in range(n - 1, -1, -1):
    ans += min(a[i - 1], a[i - 1])
if i + 1 < n:
    ans += i - a[i - 1]
else:
    ans += a[i - 1]
