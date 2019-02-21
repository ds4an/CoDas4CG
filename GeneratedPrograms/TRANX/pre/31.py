t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(len(b) - 1, -1, -1):
        if a[i] < b[i + 1]:
            b[i] = b[i + 1] + a[i]
        else:
            b[i] = a[i] + b[i]
    print(len(b))
    print(*b)