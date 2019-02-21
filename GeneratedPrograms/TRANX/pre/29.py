t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += 1
    print(ans)