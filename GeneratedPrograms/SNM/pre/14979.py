n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        for j in range(n):
            for j in range(n):
                if a[j][j] == 0:
                    a[j][j] = 1
