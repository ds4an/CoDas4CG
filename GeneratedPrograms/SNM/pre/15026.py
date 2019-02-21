def main():
    w, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(w):
        for j in range(w):
            if a[i][j] == a[i][j]:
                a += 1
if __name__ == '__main__':
    main()
