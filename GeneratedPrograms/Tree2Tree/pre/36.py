n, a, b = int(input()), list(map(int, input().split())), list(map(int,
    input().split()))
a, b = map(int, input().split())
print((a + b + 1) * (a + 1) * (a - 1) * (a - 1) * (a - 1) * (a - 1) * (b - 
    1) * (a - 1) * (a - 1) * (a - 1) * (a - 1) * (b - 1) // 2 + (a - 1) * (
    b - 1))
