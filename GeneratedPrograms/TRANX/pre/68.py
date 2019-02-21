for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(m):
        a, b = map(int, input().split())
        a[a].append(b)
        a[b].append(b)
    for i in range(m):
        a[i] = list(map(int, input().split()))
    for i in range(m):
        a, b = map(int, input().split())
        a[b].append(b)
        a[b].append(b)
    for i in range(m):
        print(a[i][0], a[i][1])