n = int(input())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(i + 1, -1, -1):
        if a[i] + a[i] > mx:
            ans = i + 1
            break
print(ans)
