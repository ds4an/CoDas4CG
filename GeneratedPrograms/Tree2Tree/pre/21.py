from math import pi
n, m = map(int, input().split())
print(sum(n - i & 1 for i in range(n)))
