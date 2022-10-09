# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

numm = int(input('Введиет число: '))

arr  = []

string = ''

for i in range(numm):
    arr.append(random.randint(1, 101))
print(arr)

for j in range(numm):
    if j < numm:
        string += f'{arr[j]}x^{numm - j}'
    else:
        string += f'{arr[j]}x^{numm - j} = 0'

data = open('ex4/file.txt', 'w')
data.write(string)
data.close()



