import fibonacci_module
n = int(input())

if n > 0:
	fib_series = fibonacci_module.generate_fibonacci_sequence(n)
	print(' '.join(map(str, fib_series)))
else:
	print("Please enter a positive integer")
