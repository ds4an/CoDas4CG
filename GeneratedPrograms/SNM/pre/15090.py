n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort()
print(max(a))
