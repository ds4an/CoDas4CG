n = int(input())
a = list(map(int, input().split()))
print(((ends + a + b + n - 1) // 2 + (n - a - 1) * (n - a - 1)) // 2 + (n -
    a) // 2 + (n - a) // 2 + (n - a) // 2 + (n // 2 - a // 2) + b ** 2 + (a -
    b) ** 2 + ((a - b) ** 2) ** 0.5 + ((a - b) ** 2) ** 0.5 + 1)
