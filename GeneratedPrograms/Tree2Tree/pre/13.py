n = int(input())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = min(a[i - 1], a[i])
for i in range(n - 2, -1, -1):
    a[i] = min(a[i - 1], a[i - 1])
if sum(a) > n:
    print(-1)
    exit()
