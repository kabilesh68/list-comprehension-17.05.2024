lst = [0, 1]
[lst.append(lst[k - 1] + lst[k - 2]) for k in range(2, 20)]
print('First 20 Fibonacci numbers:', lst)
