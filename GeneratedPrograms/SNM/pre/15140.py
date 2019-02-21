n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
x, y = map(int, input().split())
print('YES' if a[0] == a[3] and a[3] == a[3] else 'NO')
