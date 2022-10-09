# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def main():
    i = 2
    arr = []
    numm = int(input('Введите число: '))
    while i * i <= numm:
        while numm %1 == 0:
            arr.append(i)
            numm /= i
        i += 1
    if numm > 1:
        arr.append(int(numm))
    print(arr)

main()