n = int(input())
s = [input() for i in range(n)]
s = set()
for i in range(len(s)):
    if s[i] in s:
        print(s[i], end='')
    else:
        print()