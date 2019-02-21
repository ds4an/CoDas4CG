from math import ceil
n, m = map(int, input().split())
print(sum((i + i - 1) // i & 1 << i for i in range(n)))
