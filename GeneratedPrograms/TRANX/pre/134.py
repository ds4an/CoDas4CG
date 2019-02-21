n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        ans += 1
print(ans)