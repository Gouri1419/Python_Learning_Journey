print("Arithmetic Operators")
a = 10
b = 5

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation
print("a // b =", a // b) # Floor Division

print("Comparison Operators")
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

print("Logical Operators")
x = True
y = False

print(x and y) # Logical AND
print(x or y)  # Logical OR
print(not x)   # Logical NOT

print("Assignment Operators")
c = 10

c += 5         # Add and assign
print(c)

c -= 2         # Subtract and assign
print(c)

print("Identity Operators")
p = [1, 2, 3]
q = p

print(p is q)      # Same object
print(p is not q)  # Different object

print("Membership Operators")
name = "Gouri"

print("G" in name)      # Character exists
print("z" not in name)  # Character does not exist

print("Bitwise Operators")
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR