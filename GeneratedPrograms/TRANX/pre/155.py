a, b = map(int, input().split())
a, b = map(int, input().split())
a, b = map(int, input().split())
ans = 0
for i in range(b):
    a, b = map(int, input().split())
    if (a - b) % 2 == 0:
        ans += 1
print(ans)