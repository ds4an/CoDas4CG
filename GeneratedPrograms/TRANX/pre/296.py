n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: x[1])
for i in range(len(a)):
    print(a[i][i], end=' ')