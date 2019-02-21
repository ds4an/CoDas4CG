n, m = map(int, input().split())
s = list(map(int, input().split()))
s = list(map(int, input().split()))
for i in range(n):
    if s[i] == s[i]:
        s += s[i]
print(s)
