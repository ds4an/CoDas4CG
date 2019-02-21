n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += a[i] * 2
print(ans)
