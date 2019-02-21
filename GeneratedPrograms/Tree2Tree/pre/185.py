list(map(int, input().split())).split()
x, y = 0, 0
for i in range(n):
    x += x[i] * x[i]
print(-1)
