n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] = max(a[i], a[i])
c = 0
for i in range(n):
    if a[i] == a[i]:
        c += 1
print(c)
