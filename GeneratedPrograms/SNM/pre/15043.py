n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
x, y = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    a[x] += 1
print(''.join([str(x) for x in a]))
