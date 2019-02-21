n = int(input())
s = input()
ans = ''
for i in range(n):
    s = input()
    if s[i] == 'we':
        ans += 1
print('No' if ans == s else 'No')
