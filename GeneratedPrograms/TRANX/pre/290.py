for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(len(a)):
        if a[i] > a[i]:
            ans += 1
    print(ans)