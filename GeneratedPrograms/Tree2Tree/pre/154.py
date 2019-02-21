n = int(input())
( = list(map(int, input().split()))
ans = 0
for i in range(n - 1, -1, -1):
    ans += (i + 1) // 2 + (i - j & 1)
print(ans)
