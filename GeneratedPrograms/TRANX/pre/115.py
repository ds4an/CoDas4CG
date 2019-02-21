a, b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(a - 1, -1, -1):
    if a[i] < b[i + 1]:
        ans += a[i]
print(ans)