t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += a[i] - a[i - 1]
    print(c)
    t -= 1
    t -= 1
    t -= 1
