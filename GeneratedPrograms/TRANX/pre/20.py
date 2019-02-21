for _ in range(int(input())):
    n, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x, y = map(int, input().split())
        ans += abs(a[i] - a[i + 1])
        b[i + 1] -= 1
    print(ans)