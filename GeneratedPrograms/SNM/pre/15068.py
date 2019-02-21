n, m = map(int, input().split())
s = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if s[i] == s[i]:
        ans += 1
print(ans)
