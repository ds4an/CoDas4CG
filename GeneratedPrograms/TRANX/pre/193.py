n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n - 1, -1, -1):
        if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 1][j]:
            print('YES')
            exit()
print('NO')