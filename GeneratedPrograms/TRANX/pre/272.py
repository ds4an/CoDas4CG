n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(n):
    a[i] = max(a[i], a[i])
for i in range(n):
    print(a[i], end=' ')