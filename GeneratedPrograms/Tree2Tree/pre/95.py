n = int(input())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] += a[i - 1]
for i in range(n - 1, -1, -1):
    a[i] += a[i - 1]
if n - i > 0:
    ans += 1
