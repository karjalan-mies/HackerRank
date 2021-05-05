def is_leap(year):
    if year % 4:
        return 'Не високосный'
    else:
        if year % 100:
            return 'Високосный'
        else:
            if year % 400:
                return 'Не високосный'
            else:
                return 'Високосный'

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))