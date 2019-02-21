n = int(input())
a = [int(i) for i in input().split()]
print(sum((a - b) // 2 for x in a))
