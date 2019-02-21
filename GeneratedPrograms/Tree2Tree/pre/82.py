n, a, b = map(int, input().split())
s = list(map(int, input().split()))
for i in range(n):
    s += s[i] * s[i - 1]
s = sum(s[i] - s[i - 1] for i in range(n))
s = sum(s[i] - s[i - 1] for i in range(n))
s = 0
for i in range(n):
    s += s[i] * s[i - 1]
print(s)
