n, s = int(input()), list(map(int, input().split()))
a = sum((i + 1) // i & 1 for i in a)
print(s)
