n = int(input())
beams = list(map(int, input().split()))
s = sum((i + 1) // 2 * (i - 1) for i in range(1, 2 * n + 1))
s = sum((i + 1) // 2 for i in range(1, n + 1))
if s % 2 == 0:
    print(-1)
else:
    print(s)
