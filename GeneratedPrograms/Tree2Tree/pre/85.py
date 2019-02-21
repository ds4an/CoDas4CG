import math
n, m = map(int, input().split())
print(''.join(map(lambda x: (x - y) // 2 + (y - x) // 2, map(int, input().
    split()))))
