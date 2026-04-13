def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    try:
        n = int(input("Enter a number :"))
        if n < 0:
            raise ValueError
        print(f"First {n} Fibonacci Series : {list(fib(n))}")
    except ValueError:
        print("Enter a valid non-negative integer")
if __name__ == "__main__":
    main()
