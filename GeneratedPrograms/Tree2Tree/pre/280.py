n = int(input())
a = list(map(int, input().split()))
s = 0
s = 0
for i in range(1, n + 1):
    s += a[i] - s[i - 1]
    s += 1
print(s)
