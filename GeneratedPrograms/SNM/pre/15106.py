t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == '1':
            ans += 1
            ans += 1
