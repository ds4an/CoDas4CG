n, m = map(int, input().split())
a = list(map(int, input().split()))
print((a[0] + a[1] + a[1] + a[1] + a[1] + a[1] + a[1] + a[1] + a[1] + n - 1
    ) // 2 + (a[1] - a[1]) + (a[1] - a[1]) + (a[1] + a[1]) + 1)
