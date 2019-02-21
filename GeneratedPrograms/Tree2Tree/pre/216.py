from math import ceil
n, m = map(int, input().split())
print(sum(map(lambda x: x * (y - 1) // y, map(int, input().split()))))
