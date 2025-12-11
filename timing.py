def total(a,b,c):
    return a * 3600 + b * 60 + c

def main():
    a = int(input('Количество часов:'))
    b = int(input('Количество минут:'))
    c = int(input('Количество секунд:'))
    total(a,b,c)
    d = a * 3600 + b * 60 + c
    print('Суммарно секунд: ',d)
if __name__ == '__main__':
    main()

