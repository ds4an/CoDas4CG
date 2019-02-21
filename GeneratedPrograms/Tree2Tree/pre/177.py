n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] += a[i - 1]
for i in range(1, n + 1):
    ans += a[i] * a[i - 1]
if n - i > n:
    ans += 1
