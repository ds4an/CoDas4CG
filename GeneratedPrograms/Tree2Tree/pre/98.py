n = int(input())
a = [int(x) for x in input().split()]
print(['NO', 'YES'][sum(a) > sum(a)])
