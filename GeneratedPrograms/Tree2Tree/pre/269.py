from math import ceil
n, m = map(int, input().split())
print(sum((n - i) // 2 + 2 ** i for i in range(n)))
