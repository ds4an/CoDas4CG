t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    b = len(a)
    if b == b[::-1]:
        print(-1)
    else:
        print(a[a])