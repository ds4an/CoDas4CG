n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(key=lambda x: x[0])
for i in range(1, n):
    print(a[i][1], a[i][1])