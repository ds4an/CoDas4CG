n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i][j] and a[i][j] == a[i][j]:
            print(a[i][j], a[i][j])
            exit(0)
print('No')
