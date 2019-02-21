n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    ans += abs(a - b) + '\n'
print(ans)