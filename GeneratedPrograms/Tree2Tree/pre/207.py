n, k = map(int, input().split())
s = list(map(int, input().split()))
print('YES' if sum(s) == min(s) else 'NO')
