t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if a[i] == a[i]:
            c += 1
    print(c)
