n = int(input())
a = list(map(int, input().split()))
print(sum(2 ** i - 1 for i in a))
