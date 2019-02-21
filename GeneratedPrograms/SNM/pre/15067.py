n = int(input())
s = list(map(int, input().split()))
s = 0
for i in range(n):
    if s[i] == s[i]:
        s += 1
print(s)
