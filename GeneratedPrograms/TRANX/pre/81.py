n = int(input())
a = list(map(int, input().split()))
x, y = 0, 0
for i in range(len(a)):
    if a[i] == '0' and a[i] == '1':
        x += 1
    elif a[i] == 'Sergeyevna' and a[i] == '1':
        y += 1
    elif a[i] == 'Sergeyevna':
        y += 1
print(x)