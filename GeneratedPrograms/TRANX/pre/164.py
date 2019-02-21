n, t = int(input()), list(map(int, input().split()))
for i in range(int(input())):
    a, b = map(int, input().split())
    a.append(b)
    a.append(b)
for i in range(n):
    print(a[i][i], end=' ')