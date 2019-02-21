n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        ans += 1
print(ans)