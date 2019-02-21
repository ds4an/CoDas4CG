t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == a[i]:
            ans += 1
    print(ans)
    print(ans)
