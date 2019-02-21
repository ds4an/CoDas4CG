t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            s += 1
    print(s)
