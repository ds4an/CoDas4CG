a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(1, n + 1):
    ans += abs(a[i] - a[i])
print(ans)