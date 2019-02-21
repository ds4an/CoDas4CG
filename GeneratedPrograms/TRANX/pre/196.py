n = int(input())
a = []
for i in range(n):
    a.append(input().split())
a.sort()
ans = 0
for i in range(n):
    if a[i][0] == a[i][0]:
        ans += 1
print(ans)