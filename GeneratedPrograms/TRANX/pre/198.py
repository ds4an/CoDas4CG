n = int(input())
s = []
for i in range(n):
    s.append(input())
for i in range(len(s)):
    for j in range(len(s)):
        if s[i][j] == 'i':
            s += 1
print(s)