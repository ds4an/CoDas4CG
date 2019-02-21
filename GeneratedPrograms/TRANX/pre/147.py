n, k, k = map(int, input().split())
print(n * (k - 1) // 2)
for i in range(k + 1, k + 1):
    print(i + 1, i + 1, end=' ')
print()