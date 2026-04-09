def generate_fibonacci_sequence(max_value):
    fib = []
    a, b = 0, 1

    while a <= max_value:
        fib.append(a)
        a, b = b, a + b

    return fib
