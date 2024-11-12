def fibonacci_dict(n):
    fib_numbers = {0: 0, 1: 1}

    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers


print(fibonacci_dict(10))
