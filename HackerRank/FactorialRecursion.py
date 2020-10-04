def factorial(n):
    if n != 1:
        n = n * factorial(n - 1)
    return n


n = 3
result = factorial(n)
print(result)
