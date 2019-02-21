n = int(input())
a = list(map(int, input().split()))
n = int(input())
print(sum(n - i & 1 for i in range(n)))
