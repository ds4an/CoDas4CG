n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if a[i] == a[i]:
        ans += 1
