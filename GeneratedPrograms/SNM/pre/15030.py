n, m = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    if l[i] == l[i - 1]:
        ans += 1
print(ans)
