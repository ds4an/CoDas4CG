n = int(input())
a = [int(i) for i in input().split()]
print(sum(i + 1 & 2 ** i for i in a))
