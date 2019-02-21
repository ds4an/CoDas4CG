n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i][j]:
            a[j] = i + 1
print(m)
