n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
x, y = 0, 0
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[j] < a[j]:
            ans = max(ans, a[i] + a[j] + a[j])
for i in range(n):
    ans = max(ans, i + 1 - a[j])
print(ans)
