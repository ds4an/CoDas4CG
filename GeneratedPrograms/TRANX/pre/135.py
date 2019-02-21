n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    ans = (c + b) % m
    ans = max(ans, ans)
print(ans)