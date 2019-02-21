n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = max(a[i], a[i])
print(max(a[i] - a[i] for i in range(n)))
