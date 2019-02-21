n = int(input())
s = input()
ans = 0
ans = 0
for i in range(n):
    if s[i] == 'a':
        ans += 1
    ans = max(ans, ans)
print(ans)
