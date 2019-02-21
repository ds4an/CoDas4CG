for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == a[i + 1]:
            print(a[i], a[i + 1], end=' ')
    print()