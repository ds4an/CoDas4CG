a, b, c = map(int, input().split())
print(sum(c in a for c in a if c % a == 0))