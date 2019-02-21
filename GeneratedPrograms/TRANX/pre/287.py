def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()