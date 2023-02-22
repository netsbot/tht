def main():
    _ = input().split()
    a = int(_[0])
    b = int(_[1])

    print(round((a * b) - (((a / 2) ** 2) * 3.14), 2))

if __name__ == '__main__':
    main()