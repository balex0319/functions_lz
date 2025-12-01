import math
C = int(input('Введите число: '))
def number(C):
    if C % 2 == 0:
        print('Четное число')
    elif C % 2 == 1:
        print('Нечетное число')
print(number(C))
