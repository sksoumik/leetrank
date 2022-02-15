def fibonacci_series(n):
    """
    Returns the nth number in the fibonacci series
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    # print the nth number in the fibonacci series
    print(fibonacci_series(n))

    # print all the fibonacci numbers up to n
    for i in range(n):
        print(fibonacci_series(i), end=" ")

