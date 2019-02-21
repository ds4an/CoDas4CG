n, m = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(1, n + 1):
    A[i] = max(A[i], A[i - 1] + A[i - 1])
A[i] = list(map(int, input().split()))
for i in range(1, n):
    A[i] = max(A[i], A[i - 1])
print(''.join(map(str, A)))
