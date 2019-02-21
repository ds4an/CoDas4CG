n = int(input())
a = list(map(int, input().split()))
a.sort(key=lambda x: x[0])
print(a[-1][0])