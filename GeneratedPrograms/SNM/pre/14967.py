n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    x, y = map(int, input().split())
    a[x].append(y)
ans = 0
print(ans)
for i in range(n):
    print(a[i][j])
