n = int(input())
a = sorted(map(int, input().split()))
ans = 0
for i in range(n):
    ans += a[i] * a[i - 1]
print(ans)
