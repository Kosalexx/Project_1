def is_digit(num):  # проверка что введено именно число
    if str(num).isdigit():  # проверяем что введено именно число
        num = int(num)  # приводим число к int
        return num
    else:
        print('Введите целое число!')
        num = input()
        num = is_digit(num)
        return num  # рекурсия пока не будет введено целое число


# Основной цикл программы.
while True:
    name = input('Приветсвую! Введите Ваше имя: ')
    age = input('Сколько Вам лет? Введите возраст: ')
    age_2 = is_digit(age)
    print(age_2)
    while True:
        if age_2 <= 0:
            print('Ошибка, повторите ввод.')
            age = int(input('Введите коректный возраст: '))
            age_2 = is_digit(age)
            continue
        elif 0 <= age_2 < 10:
            print(f'Привет, шкет {name}.')
            break
        elif 10 <= age_2 <= 18:
            print(f'Как жизнь, {name}.')
            break
        elif 18 < age_2 <= 100:
            print(f'Что желаете, {name}.')
            break
        else:
            print(f'{name}, вы лжете - в наше время столько не живут...')
            break
    print('Хотите попробовать ещё раз?')
    ask = input('"YES" - да / Любой другой символ - нет: ')
    if ask.upper() == 'YES':
        continue
    else:
        print(f'Пока, {name}, приятно было познакомиться!')
        break
