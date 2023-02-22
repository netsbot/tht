def main():
    n = int(input())
    res1 = 0
    res2 = 0

    for i in range(n+1):
        if i >= (n-1)/2:
            res1 += 1

    res2 = n**2 - n

    
    print(res1, res2)

if __name__ == "__main__":
    main()