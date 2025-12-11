import math
def number(C):
    if C % 2 == 0:
        print('Четное число')
    elif C % 2 != 0:
        print('Нечетное число')
    
def main():
    C = int(input('Введите число: '))
    number(C)
if __name__ == '__main__':
    main()
