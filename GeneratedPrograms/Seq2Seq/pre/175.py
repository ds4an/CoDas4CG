n = int(input())
a = sorted(map(int, input().split()))
print(sum(sum(a[i]* a[i]for i in range(n))))