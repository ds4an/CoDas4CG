n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    a[x] += 1
print(x * y + y // 2 + (y - y) // 2)
