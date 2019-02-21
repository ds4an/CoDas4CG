n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
x, y = map(int, input().split())
print(sum(a[i] == a[i] for i in range(n)))
