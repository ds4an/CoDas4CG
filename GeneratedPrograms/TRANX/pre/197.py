t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1])
    for i in range(n):
        print(a[i][1], a[i][1], end=' ')
    print()