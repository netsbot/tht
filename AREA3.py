def main():
    _ = input().split()
    a = int(_[0])
    b = int(_[1])
    c = int(_[2])
    print(a * b - ((a - c + b) * c))

if __name__ == "__main__":
    main()