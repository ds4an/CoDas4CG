a, b = map(int, input().split())
if a % 2 == 0:
    print(-1)
else:
    print(min(a, b))