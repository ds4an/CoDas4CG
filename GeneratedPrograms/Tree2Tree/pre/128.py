n = int(input())
a = list(map(int, input().split()))
s = sum(a[i] - a[i - 1] for i in range(n))
s = sum(a[i] - a[i - 1] for i in range(n))
for i in range(n):
    s += a[i] * a[i - 1]
print(s)
