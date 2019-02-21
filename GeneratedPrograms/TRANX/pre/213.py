n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    if a[i] < a[i + 1]:
        a[i] = a[i + 1] + a[i]
print(' '.join(map(str, a)))