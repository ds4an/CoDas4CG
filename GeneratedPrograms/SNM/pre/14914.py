n = int(input())
a = list(map(int, input().split()))
print(sum(i - i + 1 for i in range(n)))
