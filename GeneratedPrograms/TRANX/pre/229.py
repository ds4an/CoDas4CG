n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    print(n * (n - 1) // 2)