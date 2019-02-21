n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
s = 0
for i in range(n):
    s += a[i] - a[i - 1]
print(s)
