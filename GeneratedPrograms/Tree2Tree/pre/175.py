n = int(input())
a = list(map(int, input().split()))
print('NO' if sum(sum(a[i] > a[i + 1] for i in range(n)) for j in range(n)) ==
    len(a) else 'YES')
