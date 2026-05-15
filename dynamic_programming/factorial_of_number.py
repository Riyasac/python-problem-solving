def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        n = int(input("Enter a number :"))
        if n < 0:
            raise ValueError
        print(f"Factorial of {n} is : {factorial(n)}")
    except ValueError:
        print("Enter a valid non-negative integer")

if __name__ == "__main__":
    main()
