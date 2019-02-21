n, m = map(int, input().split())
a = list(map(int, input().split()))
print(['NO', 'YES'][sum(a) % 2 == 0])
