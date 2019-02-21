t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if s[i][j] == s[i + 1][j + 1]:
                print('NO')
                break
    print(s)
