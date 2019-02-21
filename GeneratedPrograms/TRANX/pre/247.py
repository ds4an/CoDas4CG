def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] == b[i]:
            b[a[i]] -= 1
    for i in range(m):
        if a[i] == b[i]:
            print(a[i])
            break


if __name__ == '__main__':
    main()