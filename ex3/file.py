# Задайте последовательность цифр.
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random

arr =[]
numm = int(input('Введите число '))

for i in range(numm):
    arr.append(random.randint(1, 11))
print(arr)

new_arr = []
[new_arr.append(i) for i in arr if i not in new_arr]
new_arr.sort()

print(new_arr)