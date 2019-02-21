from math import ceil
n, m = map(int, input().split())
print(sum(sum(i - j & 2 << j for i in range(n)) for j in range(n)))
