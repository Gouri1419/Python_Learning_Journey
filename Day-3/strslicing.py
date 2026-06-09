fruit = "Watermelon"

print(fruit[0:5])     # Water
print(fruit[5:10])    # melon

print(fruit[:5])      # Water      (start omitted)
print(fruit[2:])      # termelon   (end omitted)
print(fruit[:])       # Watermelon (whole string)

print(fruit[3:8])     # ermel

print(fruit[-5:])     # melon
print(fruit[:-5])     # Water
print(fruit[-8:-3])   # terme

print(fruit[::1])     # Watermelon (step = 1)
print(fruit[::2])     # Wtrln      (every 2nd character)
print(fruit[::3])     # Wrmn       (every 3rd character)

print(fruit[1::2])    # aeeo       (start at index 1, step 2)

print(fruit[::-1])    # nolemretaW (reverse string)
print(fruit[::-2])    # nlmrtW     (reverse, every 2nd character)

print(fruit[2:8:2])   # trm        (start:end:step)
print(fruit[1:9:3])   # aro        (every 3rd char from index 1 to 8)