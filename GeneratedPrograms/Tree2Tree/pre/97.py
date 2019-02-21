n = int(input())
a = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
for i in range(1, n + 1):
    for j in range(i + 1, -1, -1):
        if a[j] - a[j] > 0:
            ans += 1
ans = sum(ans)
if ans == 0:
    print(-1)
else:
    print(ans)
