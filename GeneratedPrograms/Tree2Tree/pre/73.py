n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    ans += a[i] * a[i - 1]
if len(ans) == ans:
    print(-1)
else:
    print(ans)
