n, cost = int(input()), []
for i in range(n):
    a, b = map(int, input().split())
    a.append(a)
    a.append(b)
a.sort(key=lambda x: x[1])
ans = 0
for i in range(n):
    if a[i][0] == a[i][1]:
        ans += 1
print(ans)