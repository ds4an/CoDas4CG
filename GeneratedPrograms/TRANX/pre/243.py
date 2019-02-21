for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += 1
    print(ans)