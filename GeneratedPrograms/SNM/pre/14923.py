n = int(input())
a = list(map(int, input().split()))
while n % 2 == 0:
    n -= 1
print(sum(a))
