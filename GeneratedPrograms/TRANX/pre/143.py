n, m = [int(i) for i in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] > a[i][j]:
            ans += 1
print(ans)