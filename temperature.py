import math
print('Введите температуру в градусах по Цельсию: ')
T = float(input())
def temperature(T):
    return T * 1.8 + 32
a = temperature(T)
a = T * 1.8 + 32
print ('Температура в градусах по Фаренгейту: ',a)