n = int(input())
a = list(map(int, input().split()))
s = set()
for i in range(n):
    a.append(input().split())
for i in range(len(s)):
    if s[i] not in s:
        print(s[i], end='')
    print()