n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
y = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i + 1][i + 1]:
            y += 1
print(x)
