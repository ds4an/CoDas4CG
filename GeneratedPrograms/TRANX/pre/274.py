for _ in range(int(input())):
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == a[i][j]:
                ans += 1
    print(ans)