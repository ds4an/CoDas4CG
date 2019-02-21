n = int(input())
a = list(map(int, input().split()))
print(sum(n - i & 1 for i in a))
