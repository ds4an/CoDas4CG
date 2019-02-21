l = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
if sum(l[i] - l[i - 1] for i in range(1, n + 1)) == l:
    print(-1)
else:
    print(-1)
