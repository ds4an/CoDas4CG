def main():
    a, b = [int(x) for x in input().split()]
    a = []
    for i in range(5):
        a.append(int(input()))
    a.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(5):
        if a[i][0] == 1:
            a[i][3] += a[i][3]
            a[i][3] += a[i][3]
    if a[0][0] == 1:
        print(a[0][0], a[3][1], a[3][1], a[3][1], a[3][1], a[3][1], a[3][1],
            a[3][1], a[3][1], a[3][1], a[3][1], a[3][1], a[3][1], a[3][1],
            a[3][1], a[3][1], a[3][1], a[3][1], a[3][])