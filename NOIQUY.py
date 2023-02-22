def main():
    _ = input().split()
    a = int(_[0])
    b = int(_[1])
    c = int(_[2])

    t = int(_[3])
    n = int(_[4])
    m = int(_[5])

    print((a * t) + (b * n) + (c * m))

if __name__ == '__main__':
    main()