n, n = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    a[a - 1] += 1
    a[b - 1] += 1
for i in range(n):
    a, b = map(int, input().split())
    a[a - 1] += 1
    a[b - 1] += 1
for i in range(n):
    print(a[i], end=' ')