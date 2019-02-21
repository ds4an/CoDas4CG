n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(key=lambda x: x[1])
if a[0][0] == 1:
    print(a[-1][1], a[-1][1], a[-1][1])
else:
    print(a[-1][1])