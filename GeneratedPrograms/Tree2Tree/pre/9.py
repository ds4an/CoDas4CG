n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(a.index(max(a)))
