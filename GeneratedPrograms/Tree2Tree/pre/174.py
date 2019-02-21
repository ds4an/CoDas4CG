n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += (i + 1) * a[i]
print(ans)
