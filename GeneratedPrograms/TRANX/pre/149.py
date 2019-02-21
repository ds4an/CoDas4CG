n, k = [int(i) for i in input().split()]
a = [int(x) for x in input().split()]
for i in range(n):
    if a[i] == a[i]:
        print(a[i], end=' ')