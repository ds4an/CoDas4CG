n = int(input())
a = sorted([int(input()) for _ in range(n)])
print(sum(2 ** i - 1 for i in a))
