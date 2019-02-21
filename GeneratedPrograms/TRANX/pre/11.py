R = lambda : list(map(int, input().split()))
n, k = R()
a = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    a[a - 1] += 1
    a[b - 1] += 1
print(' '.join(map(str, a)))