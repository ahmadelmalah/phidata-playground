def fibonacci(n):
    a, b = 0, 1
    result = [a, b]
    for i in range(2, n):
        c = a + b
        result.append(c)
        a, b = b, c
    return result

def display_fibonacci(n):
    result = fibonacci(n)
    print(f"Fibonacci series till the {n}th number:", result)

n = 10
display_fibonacci(n)