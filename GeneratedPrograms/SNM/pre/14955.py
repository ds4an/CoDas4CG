n = int(input())
a = list(map(int, input().split()))
ans = sum([(i - i) for i in range(n)])
print(len(ans))
