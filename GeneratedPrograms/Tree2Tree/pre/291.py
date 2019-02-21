n, m = map(int, input().split())
a = list(map(int, input().split()))
print(sum(2 ** i - 1 & 2 ** i for i in range(n)))
