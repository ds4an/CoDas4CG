n, m = map(int, input().split())
s = list(map(int, input().split()))
ans = 0
for i in range(m):
    x, y = map(int, input().split())
    if x == 1:
        ans += 1
print(ans)
