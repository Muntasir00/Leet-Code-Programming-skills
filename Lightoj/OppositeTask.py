def main():
    cases = int(input())
    for caseno in range(1, cases + 1):
        n = int(input())
        if(n>10):
            print(10,n-10)
        else:
            print(0,n)

# Run the program
main()
