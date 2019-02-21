l = map(int, input().split())
a, b = (a + b + 1) // 2, (a + b + 1) // 2
a, b = (a + b) // 2, (a + b) // 2
if a < b:
    c += 1
print(c)
