n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')