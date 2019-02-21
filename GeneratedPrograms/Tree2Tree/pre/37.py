n = int(input())
a = list(map(int, input().split()))
print(sum((i + 1) // 2 + (i - i) // 2 for i in range(n - 1)))
