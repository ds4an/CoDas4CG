n = int(input())
a = list(map(int, input().split()))
x, y = 0, 0
x, y = map(int, input().split())
x, y = 0, 0
x, y = map(int, input().split())
for i in range(n):
    for j in range(i + 1, y + 1):
        if a[i] < a[j]:
            x += 1
for i in range(n):
    x += x[i] * x[i]
print(x)
