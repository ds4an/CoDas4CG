a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if a[i] == b[i + 1]:
        c += 1
print(c)