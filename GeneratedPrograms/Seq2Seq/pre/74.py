n = int(input())
a =[set(map(int, input().split()))for i in range(n)]
print('YES' if any(a[i]in a[j]else 'NO')