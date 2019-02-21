n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = a[i - 1] + a[i - 1]
print(a[n - 1])
print('\n'.join(map(str, a)))
