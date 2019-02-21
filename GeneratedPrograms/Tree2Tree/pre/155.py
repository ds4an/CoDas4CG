n, k = map(int, input().split())
print(min(((n - i - 1) // m + 1) // k for i in range(n)))
