n = int(input())
for i in range(n):
    s = input()
    i = 0
    for i in range(len(s)):
        if s[i] == s[i]:
            count += 1
    print(count)
