lst = [1, 2, 5, -11, -9, 10, 13, 15, -17, -19, -21, -23, 25, 27, -29]
pos = [num for num in lst if num > 0]
print(pos)
neg = [num for num in lst if num < 0]
print(neg)
output:
[1,2,5,10,13,15,25,27]
[-11,-9,-17,-19,-21,-23,-29]
