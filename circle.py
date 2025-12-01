import math 
R = float(input('Введите радиус круга в см:'))
def length(R):
    return 3.14*2*R
a = length(R)
a = 3.14*2*R
print('Длина окружности:',a)

def square(R):
    return 3.14*R**2
b = square(R)
b = 3.14*R**2
print('Площадь окружности:' ,b)

def main():
    R = float(input())
    a = length(R)
    b = square(R)
if __name__ == '__main__':
    main()

