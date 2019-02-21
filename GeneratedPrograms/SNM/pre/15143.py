n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == a[i][j]:
            s += 1
print(s)
