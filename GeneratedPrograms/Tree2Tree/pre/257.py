a, b = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
    s += a[i] - a[i - 1]
print(s)
