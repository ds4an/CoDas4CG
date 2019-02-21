a, b = map(int, input().split())
a, b = sorted(map(int, input().split())), list(map(int, input().split()))
a, b = min(a, b), min(a, b)
print(a + b - 1)