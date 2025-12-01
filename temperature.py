import math
T = float(input('Введите температуру в градусах по Цельсию: '))
def temperature(T):
    return T * 1.8 + 32
a = temperature(T)
a = T * 1.8 + 32
print ('Температура в градусах по Фаренгейту: ',a)

def main():
    T = float(input())
    a = temperature(T)
if __name__ == '__main__':
    main()
