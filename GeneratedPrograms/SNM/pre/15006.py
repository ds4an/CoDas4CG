n, m = map(int, input().split())
s = input()
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    if s == 'height':
        ans += 1
print(ans)
