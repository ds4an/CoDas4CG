import math
n, m = map(int, input().split())
print(math.ceil((math.ceil(n / 2 + n / 2) + n) / 2))
