n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = max(a)
print('-1' if a[0][1] == a[1][1] and a[1][1] == a[1][1] else '-1')
