n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i + 1, n + 1):
        if a[i][j] == a[i][j] and a[i][j] == a[i + 1][j]:
            a[i][j] += 1
print(' '.join(map(str, a)))