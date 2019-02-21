n, m = map(int, input().split())
p = list(map(int, input().split()))
s = set()
for i in range(n):
    x, y = map(int, input().split())
    d[x - 1] += 1
    d[x + 1] += 1
print(d[n - 1])