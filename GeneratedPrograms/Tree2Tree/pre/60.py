n = int(input())
a = [int(x) for x in input().split()]
print(sum(sum(x > y for x in a) for x in a))
