import math
def temperature(T):
    return T * 1.8 + 32

def main():
    T = float(input('Введите температуру в градусах по Цельсию: '))
    a = temperature(T)
    print ('Температура в градусах по Фаренгейту: ',a)
if __name__ == '__main__':
    main()
