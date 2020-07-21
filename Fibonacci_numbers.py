# Generating and printing Fibonacci numbers below 1000000000000000.

a, b = 0, 1

while a < 1000000000000000:
    print(a)
    a, b = b, a + b
