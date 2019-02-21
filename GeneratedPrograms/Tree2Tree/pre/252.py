n = int(input())
a = [int(i) for i in input().split()]
print(sum(n - i <= n for i in a))
