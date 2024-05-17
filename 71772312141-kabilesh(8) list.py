import random
rows, cols = (5, 4)
arr = [[(4 * random.randint(10, 40)) for i in range(cols)] for j in
range(rows)]
print(arr)
