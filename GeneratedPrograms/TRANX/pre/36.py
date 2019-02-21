n, k, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    ans += abs(a[a] - a[b - 1])
print(ans)