for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(len(b) - 1, -1, -1):
        if b[i] == b[i]:
            ans += 1
    print(ans)