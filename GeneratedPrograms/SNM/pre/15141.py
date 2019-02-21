n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and a[i][j] == 1:
            print('YES')
            break
print('YES')
