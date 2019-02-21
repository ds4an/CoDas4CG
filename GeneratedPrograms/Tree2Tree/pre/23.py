from collections import Counter
n, m = map(int, input().split())
print(sum(n - i - 1 & 2 ** i for i in range(n)))
