a, b = map(int, input().split())
for i in range(a):
    a, b = input().split()
    a, b = int(a), int(b)
    if b == '1':
        print(a, end='')
        exit()
print('NO')