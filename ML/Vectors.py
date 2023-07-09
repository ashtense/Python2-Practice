from numpy import array
v = array([1, 2, 3])
print(v)

# Vector arithmetic example
print('Vector addition example')
a = array([1, 2, 3])
b = array([1, 2, 3])
print('Sample vectors:', a, b)
c = a + b
print('Addition', c)
d = a - b
print('Subtraction', d)
m = a * b
print('Multiplication', m)
# Vector dot product - Sum of multiplied elements from both vectors
# dot_product = a.dot(b) # Old implementation of the dot operator from numpy library
dot_product = a @ b
print('Dot Product', dot_product)
# Vector scalar multiplication - In effect scaling the magnitude of the vector
scal_multiply = a * 0.3
print('Scalar multiplication', scal_multiply)