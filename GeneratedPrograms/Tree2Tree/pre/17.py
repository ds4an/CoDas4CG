n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(1, n + 1):
    s += a[i] * a[i - 1]
print(s)
print(s)
