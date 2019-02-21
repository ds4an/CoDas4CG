n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if a + b > 0:
        a, b = b, b
    a, b = b - 1, b - 1
print(a + 1)