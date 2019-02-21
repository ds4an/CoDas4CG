n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if a[i][i] == 0:
            a[i][i] += 1
            a[i][i] += 1
print(m)
