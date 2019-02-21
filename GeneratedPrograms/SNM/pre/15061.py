n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
print(max(x - y + 1, y - x))
