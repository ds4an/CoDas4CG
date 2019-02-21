n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(0, n):
    if a[i] == 0:
        ans += 1
print(ans)