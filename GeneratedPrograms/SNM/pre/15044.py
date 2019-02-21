a, b, c = map(int, input().split())
ans = 0
for i in range(1, a + 1):
    ans = max(ans, i * i + i * i * d)
print(ans)
print(ans)
