t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(len(s)):
        if s[i] == s[i]:
            count += 1
