n = int(input())
a = sorted(map(int, input().split()))
c = sum(a)
if n % 2 == 0:
    c += 1
print(c)
