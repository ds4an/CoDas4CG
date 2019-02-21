n = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
x, y = map(int, input().split())
x, y = map(int, input().split())
c = [0] * n
for i in range(n):
    a[i] = min(a[i], a[i])
for i in range(n - 1, -1, -1):
    a[i] = a[i] + 1
print(''.join(map(str, a)))
