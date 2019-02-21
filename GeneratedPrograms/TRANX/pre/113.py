n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == a[i + 1][j]:
            a[i][j] = a[i + 1][j]
print(''.join(map(str, a)))