n, m = map(int, input().split())
a = list(map(int, input().split()))
print(sum((a - i + 1) // i for i in range(n)))
