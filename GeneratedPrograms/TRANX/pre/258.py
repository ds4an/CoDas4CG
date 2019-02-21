n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    if a[i][0] < a[i][1]:
        print(a[i][1], a[i][1], a[i][1], a[i][1])
        exit()
print(-1)