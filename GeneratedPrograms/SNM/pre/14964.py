t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i] == 0:
            ans += a[i]
    print(ans)
