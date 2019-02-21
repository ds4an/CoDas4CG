n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if a[i] == a[i]:
        c += 1
print(c)
