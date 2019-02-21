s = list(map(int, input().split()))
n = s // 2 + 1
x = x // 2 + 1
y = x // 2 + y // 2
y = (y - x) // 2
print(y)
