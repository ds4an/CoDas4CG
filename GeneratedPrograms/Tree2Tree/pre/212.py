n, x, y = map(int, input().split())
a = list(map(int, input().split()))
print(sum(i + 1 & (i + 1 > x) for i in range(i + 1, n, i)))
