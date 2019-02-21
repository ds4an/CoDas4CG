n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if l[i] == 1:
        ans += 1
print(ans)
