n = int(input())
l = list(map(int, input().split()))
ans = ''
for i in range(n):
    if l[i] == l[i - 1]:
        ans = ans + 1
if ans == ans:
    print('-1')
else:
    print('-1')
