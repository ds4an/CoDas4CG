n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum((a - b) // 2 for c in a))
