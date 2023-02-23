def main():
    _ = input()
    n = int(_.split()[0]) + int(_.split()[1]) + int(_.split()[2]) + int(_.split()[3])
    
    
    print(n)
    print(str(n)[len(str(n)) - 2], str(n)[len(str(n))-1])
    
if __name__ == '__main__':
    main()
