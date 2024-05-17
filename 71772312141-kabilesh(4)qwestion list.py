lst1 = [x for x in range(40) if x % 2 != 0]
print('First 20 Odd Numbers:')
print(lst1)
lst2 = [x for x in range(40) if x % 2 == 0]
print('First 20 Even Numbers:')
print(lst2)
output:
First 20 Odd Numbers:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
First 20 Even Numbers:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
