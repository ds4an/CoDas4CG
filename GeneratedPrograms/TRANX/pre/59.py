n, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(key=lambda x: x[0])
if a[-1][0] == a[-1][1]:
    print(-1)
else:
    print(a[-1][0], a[-1][1])