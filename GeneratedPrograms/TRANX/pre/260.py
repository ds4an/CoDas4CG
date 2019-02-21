n = int(input())
s = input()
ans = 0
for i in range(len(s)):
    if s[i] == s[i]:
        ans += 1
print(ans)