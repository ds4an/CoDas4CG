n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i][j] and a[i][j] == a[i][j]:
            print('YES')
            exit()
print('NO')