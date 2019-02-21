n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(key=lambda x: x[1])
print(a[-1][0])