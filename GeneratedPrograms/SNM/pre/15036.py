n, m = map(int, input().split())
t = list(map(int, input().split()))
t = list(map(int, input().split()))
t = list(map(int, input().split()))
for i in range(n):
    t[i] = max(t[i], t[i])
print(max(t[i] + t[i] for i in t))
