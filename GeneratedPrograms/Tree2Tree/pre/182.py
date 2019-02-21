n = int(input())
a = [int(x) for x in input().split()]
print(sum(i + 1 & i - 1 for i in a))
