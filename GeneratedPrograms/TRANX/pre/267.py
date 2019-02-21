n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(a) == 1:
    print(-1)
else:
    print(len(a))