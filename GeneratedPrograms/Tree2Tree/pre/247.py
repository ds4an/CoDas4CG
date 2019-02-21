n = int(input())
a = list(map(int, input().split()))
print(['NO', 'YES'][sum(i + i & 1 for i in a) % 2 == 0])
