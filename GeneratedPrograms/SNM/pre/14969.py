n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(a)):
    a[i] = a[i] + a[i]
print(a[0])
