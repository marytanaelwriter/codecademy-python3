# Your code below:

single_digits = range(0,10)

squares = []

for digit in single_digits:
  squares.append(digit**2)
  print(digit)

print(squares)

cubes = []

for digit in single_digits:
  cubes.append(digit**3)
  print(cubes)

# List comprehension

cubes = [digit ** 3 for digit in single_digits]
print(cubes)
