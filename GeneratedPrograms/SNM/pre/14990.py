n = int(input())
count = 0
for i in range(n):
    s = input()
    if s[-1] == s[-1]:
        count += 1
print(count)
