n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] <= a[i]:
        ans += a[i] - a[i]
print(ans)
