n, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n - 1, -1, -1):
        if t[i][j] == t[i + 1][j]:
            ans += 1
print(ans)