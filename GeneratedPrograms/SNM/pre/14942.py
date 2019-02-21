n = int(input())
a = list(map(int, input().split()))
print(max(a * b + a * b for a, b in enumerate(a)))
