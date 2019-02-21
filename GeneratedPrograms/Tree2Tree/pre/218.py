n = int(input())
a = [int(x) for x in input().split()]
print(sum(2 ** i - 1 & 2 ** i for i in a))
