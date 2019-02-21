n = int(input())
a = list(map(int, input().split()))
print(sum(i * n - i * n for i in a))
