n = int(input())
a = [int(x) for x in input().split()]
s = sorted([int(i) for i in input().split()])
for i in range(n):
    s += a[i] * a[i - 1]
s = sum(a[i] - a[i - 1] for i in range(n - 1, -1, -1))
s = sorted(list(map(int, input().split())))
while s[0] > 0:
    s += 1
print(s)
print(s)
