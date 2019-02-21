n, m = map(int, input().split())
a = list(map(int, input().split()))
n, m = map(int, input().split(''))
if (n // 2 + n * 2 + n - 1
    ) ** 0.5 + 0.5 ** 0.5 + 0.5 ** 0.5 + 0.5 ** 0.5 + 0.5 ** 0.5 <= m:
    print(-1)
else:
    print(n)
print(m)
