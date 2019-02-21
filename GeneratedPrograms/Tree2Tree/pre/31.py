import math
n = int(input())
print(sum((x + y) % 2 for x in range(1, n + 1)))
