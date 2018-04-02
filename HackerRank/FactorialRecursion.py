def factorial(n):
    if n != 1:
        n = n * factorial(n - 1)
    return n


n = int(raw_input().strip())
result = factorial(n)
print result
