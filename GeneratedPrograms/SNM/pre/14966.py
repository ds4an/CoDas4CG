n = int(input())
a = list(map(int, input().split()))
print('YES' if a[0] == a[1] and a[1] == a[1] else 'NO')
