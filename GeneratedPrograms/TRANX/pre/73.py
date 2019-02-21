a, b = map(int, input().split())
ans = 0
for i in range(1, a + 1):
    ans *= i
print(ans)