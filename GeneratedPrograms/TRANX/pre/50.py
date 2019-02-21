a, b = int(input()), list(map(int, input().split()))
if len(a) == 1:
    print(-1)
else:
    for i in range(a - 1, -1, -1):
        if a[i] == a[i + 1] and a[i] == a[i + 1]:
            print(i + 1)
            break
    else:
        print(-1)