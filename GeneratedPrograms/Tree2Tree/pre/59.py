n = int(input())
letters = [int(i) for i in input().split()]
print(sum(i - i & 1 for i in range(n)))
