from math import sqrt

def main():
    a = int(input())
    print(round(a ** 2 * (4 * 3.14 - 3 * sqrt(3)) / 12, 2))

if __name__ == "__main__":
    main()