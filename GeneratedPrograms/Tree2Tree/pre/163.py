n = int(input())
s = list(map(int, input().split()))
print(sum(i & 1 for i in s) // 2)
