a = int(input('Количество часов:'))
b = int(input('Количество минут:'))
c = int(input('Количество секунд:'))
def total(d):
    return a * 3600 + b * 60 + c
d = a * 3600 + b * 60 + c
print('Суммарно секунд: ',d)

def main():
    total(d)
if __name__ == '__main__':
    main()