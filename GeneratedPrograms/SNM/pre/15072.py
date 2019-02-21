n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(-1)
else:
    print(''.join(map(str, a)))
