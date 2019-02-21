n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
x, y = int(input()), list(map(int, input().split()))
print(['NO', 'YES'][x[0] == x[2] and x[3]])
