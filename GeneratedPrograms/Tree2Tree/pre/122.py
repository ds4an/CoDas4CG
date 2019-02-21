n = int(input())
a = list(map(int, input().split()))
s = sum(a[i] - a[i - 1] for i in range(n))
ans = sum(a[i] - a[i - 1] for i in range(n))
for i in range(n - 2, -1, -1):
    ans = max(ans, a[i] + a[i - 1])
print(ans)
