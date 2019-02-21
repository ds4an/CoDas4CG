n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = [int(x) for x in input().split()]
print(''.join([str(x) for x in a]))
