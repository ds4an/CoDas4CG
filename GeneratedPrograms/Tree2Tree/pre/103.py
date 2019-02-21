n = int(input())
s = list(map(int, input().split()))
s = list(map(int, input().split()))
s = 0
for i in range(n):
    s += s[i] * s[i - 1]
print(s)
