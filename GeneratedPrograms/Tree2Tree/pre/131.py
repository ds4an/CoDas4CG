n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split('')]
c = [int(x) for x in input().split()]
ans = 0
ans = 0
for i in range(n):
    if a[i] != a[i - 1]:
        ans += 1
    ans = max(ans, ans)
for i in range(n - 1, -1, -1):
    ans = max(ans, i + j + 1)
print(ans)
