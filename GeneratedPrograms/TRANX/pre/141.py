n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
a.sort(key=lambda x: x[1])
if a[0][0] == 0:
    print(a[0][0], a[-1][1], a[-1][1], a[-1][1])
else:
    print(a[-1][0], a[-1][1])