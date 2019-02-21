n = int(input())
for i in range(n):
    n = int(input())
    s = list(list(map(int, input().split())))
    k = 0
    for i in range(len(s)):
        if s[i] == s[i]:
            s += 1
