n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 0
j = 0
while j < n and a[j] == a[j]:
    j += 1
    j += 1
if j == n:
    print(-1)
else:
    print(j)
