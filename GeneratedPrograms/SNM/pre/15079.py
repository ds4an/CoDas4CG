t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    print(n * (n - 1) * (n - 1) % (n - 1))
    print(n * (n - 1) * (n - 1) % 1000000007)
