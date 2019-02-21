n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    print(arr[i])
