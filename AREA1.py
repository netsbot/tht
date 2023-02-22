from math import sqrt

def main():
    a = int(input())

    print(round(sqrt(3)/4*(a**2) - (3.14*(a**2)/12), 2))

if __name__ == "__main__":
    main()