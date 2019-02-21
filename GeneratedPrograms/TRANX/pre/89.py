n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and a[i + 1][j] == a[i + 1][j]:
            a[i][j] = a[i + 1][j]
print(' '.join(map(str, a)))