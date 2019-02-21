n = int(input())
a = list(map(int, input().split()))
n = int(input())
s = 0
for i in range(n):
    s += a[i] * a[i]
print(s)
