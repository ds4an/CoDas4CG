t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1, -1, -1):
        if a[i] == b[i + 1]:
            ans += 1
    print(ans)