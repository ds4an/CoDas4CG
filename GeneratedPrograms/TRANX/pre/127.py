t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == a[i]:
            print(a[i], end=' ')
    print()