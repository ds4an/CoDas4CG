n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        print(a + b, end='')
        exit()
print('NO')