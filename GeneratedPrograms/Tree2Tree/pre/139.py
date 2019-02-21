n = int(input())
a = [int(i) for i in input().split()]
print(sum(2 ** i - 1 for i in a))
