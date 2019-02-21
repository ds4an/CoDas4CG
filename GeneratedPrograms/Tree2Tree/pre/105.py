from collections import Counter
n, k = map(int, input().split())
print(sum(sum(x[::-1] > x for x in map(int, input().split())) for _ in
    range(n)))
