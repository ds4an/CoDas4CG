n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a + b + 1 + (a - b) // 2)
