n = int(input())
a = [int(x) for x in input().split()]
a.sort()
for i in range(1, n + 1):
    print(a[i], end=' ')