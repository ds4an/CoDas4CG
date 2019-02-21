n, m = map(int, input().split())
s = list(input())
i = 0
for i in range(len(s)):
    if s[i] == s[i - 1]:
        s += 1
print(s)
