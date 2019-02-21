n = int(input())
s = list(map(int, input().split()))
while n % 2 == 0:
    s += 1
print(s)
