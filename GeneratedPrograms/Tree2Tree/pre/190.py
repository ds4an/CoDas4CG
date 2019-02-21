n = int(input())
a = [int(x) for x in input().split()]
print(sum(sum(x > y for x in a) > sum(a) for x in a))
