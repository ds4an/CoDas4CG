n = int(input())
a = list(map(int, input().split()))
if sum(a[i] - a[i - 1] for i in range(n)) == 1:
    print(-1)
else:
    print(''.join(map(str, a)))
