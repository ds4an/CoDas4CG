n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
print('YES' if sum(a) == sum(b) else 'NO')
