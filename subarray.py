from numpy import *

values = [1, 2, 3, -3, 0, 5, 6, 7, 8]
given = 11
array1 = []
array2 = []
array3 = []
array4 = array([0] * 5)
loop = 2 ** len(values) - 1
for i in range(1, loop + 1):
    binary = bin(i)
    for j in binary:
        array1.append(j)
    for k in range(2, len(array1)):
        array2.append(array1[k])
    array2.reverse()
    for m in range(len(array2)):
        num = int(array2[m]) * int(values[m])
        if num != 0:
            array3.append(num)
    sum = 0
    for n in range(len(array3)):
        sum += int(array3[n])
    if sum == given:
        if len(array3) <= len(array4):
            array4 = array3.copy()
    array1.clear()
    array2.clear()
    array3.clear()
print(array4)
