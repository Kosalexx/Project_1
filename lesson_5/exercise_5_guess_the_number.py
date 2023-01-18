import random


def is_digit(num):  # проверка что введено именно число. Будем использовать при задании дового диапазона.
    if num.isdigit():  # проверяем что введено именно число
        num = int(num)  # приводим число к int
        return num
    else:
        print('Введите целое число!')
        num = input()
        num = is_digit(num)  # рекурсия пока не будет введено целое число
        return num


def is_valid(num, st, en):  # проверка введённого числа на коректность. Используем при отгадывании.
    if num.isdigit():  # проверяем что введено именно число
        num = int(num)  # приводим к int
        if st <= num <= en:  # проверка что число лежит в указанном диапазоне
            return True
        else:
            return False
    else:
        return False


# Начало. Приветствие и замена диапазона (если требуется).

print('''Привет! Сыграем в игру?)
Мы загадали число от 1 до 100 и ты должен его отгадать!
Если вдруг ты хочешь изменить диапазон, в котором загадано число - напиши "YES"!''')
ans = input('Меняем? (YES - да / любая кнопка - нет): ')
if ans.upper() == 'YES':  # цикл для изменения диапазона
    start_range = input('Начало нового диапазона: ')
    start_range = is_digit(start_range)
    end_range = input('Конец нового диапазона: ')
    end_range = is_digit(end_range)
    if start_range >= end_range:  # проверка больше ли конец диапазона чем его начало
        print('Конец заданного диапазона должен быть больше его начала!')
        while start_range > end_range:
            end_range = input('Конец нового диапазона: ')
            end_range = is_digit(end_range)
else:
    start_range = 1
    end_range = 100

print(f'Итак, начнём! Мы загадали число от {start_range} до {end_range}.')
print('Если захочешь остановиться - введи слово "stop"')
secret_number = random.randint(start_range, end_range)  # генерация числа в указанном диапазоне
counter = 0  # заведём счётчик попыток

# основной цикл программы:
while True:
    attempt = input('Введи число от {} до {}: '.format(start_range, end_range))
    if attempt.lower() == 'stop':  # способ завершить программу если не получается отгадать
        print('Ещё увидимся!')
        break
    elif not is_valid(attempt, start_range, end_range):
        print(f'Нужно ввести целое число в диапазоне от {start_range} до {end_range}!')
        continue
    attempt = int(attempt)

    if attempt > secret_number:
        print('Загаданное число меньше твоего. Попробуй ещё раз!')
        counter += 1
    elif attempt < secret_number:
        print('Загаданное число больше твоего. Попробуй ещё раз!')
        counter += 1
    else:
        counter += 1
        print(f'Ты угадал! Молодец! Количество попыток: {counter}.')
        counter = 0
        break
