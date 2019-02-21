n = int(input())
a = list(map(int, input().split()))
print('Yes' if sum(a[: i])== 0 else 'No')