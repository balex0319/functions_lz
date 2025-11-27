import math 
print('Введите радиус круга в см:')
R = float(input())
def length(R):
    return 3.14*2*R
a = length(R)
a = 3.14*2*R
def square(R):
    return 3.14*R**2
b = square(R)
b = 3.14*R**2

def main():
    a = length(R)
    b = square(R)
    print('Длина окружности:',a)
    print('Площадь окружности:' ,b)
if __name__ == '__main__':
    main()