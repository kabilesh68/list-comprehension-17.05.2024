lst = [0, 1]
[lst.append(lst[k - 1] + lst[k - 2]) for k in range(2, 20)]
print('First 20 Fibonacci numbers:', lst)
output:
First 20 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
