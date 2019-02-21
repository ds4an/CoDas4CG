n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    x.append(y)
y = 0
for i in range(n):
    x, y = map(int, input().split())
    if x == y:
        y += 1
print('Yes' if x == y else 'No')
