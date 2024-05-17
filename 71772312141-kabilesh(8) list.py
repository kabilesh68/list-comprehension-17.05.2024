import random
rows, cols = (5, 4)
arr = [[(4 * random.randint(10, 40)) for i in range(cols)] for j in
range(rows)]
print(arr)
output:
[[60, 136, 92, 160], [112, 160, 140, 112], [152, 64, 84, 152], [128, 92, 116, 60], [56, 148, 88, 116]]
