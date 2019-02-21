n = int(input())
s = list(map(int, input().split()))
print(max((n - i + 1) // n for i in range(n)))
