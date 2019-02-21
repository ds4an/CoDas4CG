s = input()
n = len(s)
ans = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == s[i]:
        ans += 1
print(ans)