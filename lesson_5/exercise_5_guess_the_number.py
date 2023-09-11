import random


def is_digit(number: str) -> int:  # проверка что введено именно число.
    if number.isdigit():  # проверяем что введено именно число
        new_num = int(number)  # приводим число к int
        return new_num
    else:
        print('Введите целое число!')
        number = input()
        new_num = is_digit(number)
        return new_num


def is_valid(
        number: str,
        start: int,
        end: int) -> bool:  # проверка введённого числа на коректность.
    if number.isdigit():  # проверяем что введено именно число
        new_num = int(number)  # приводим к int
        if start <= new_num <= end:
            return True
        else:
            return False
    else:
        return False


print('Привет! Сыграем в игру?) \n'
      'Мы загадали число от 1 до 100 и ты должен его отгадать!'
      'Если вдруг ты хочешь изменить диапазон, в котором загадано'
      'число - напиши "YES"!')

ans = input('Меняем? (YES - да / любая кнопка - нет): ')
if ans.upper() == 'YES':
    start_range = input('Начало нового диапазона: ')
    new_start_range = is_digit(start_range)
    end_range = input('Конец нового диапазона: ')
    new_end_range = is_digit(end_range)
    if new_start_range >= new_end_range:
        print('Конец заданного диапазона должен быть больше его начала!')
        while new_start_range >= new_end_range:
            end_range = input('Конец нового диапазона: ')
            new_end_range = is_digit(end_range)
else:
    new_start_range = 1
    new_end_range = 100

print(f'Итак, начнём! Мы загадали число от {new_start_range} до'
      f' {new_end_range}.')
print('Если захочешь остановиться - введи слово "stop"')
secret_number = random.randint(new_start_range, new_end_range)
counter = 0

# основной цикл программы:
while True:
    attempt = input('Введи число от {} до {}: '.format(new_start_range,
                                                       new_end_range))
    if attempt.lower() == 'stop':
        break
    elif not is_valid(attempt, new_start_range, new_end_range):
        print(f'Нужно ввести целое число в диапазоне от'
              f' {start_range} до {end_range}!')
        continue
    final_attempt = int(attempt)

    if final_attempt > secret_number:
        print('Загаданное число меньше твоего. Попробуй ещё раз!')
        counter += 1
    elif final_attempt < secret_number:
        print('Загаданное число больше твоего. Попробуй ещё раз!')
        counter += 1
    else:
        counter += 1
        print(f'Ты угадал! Молодец! Количество попыток: {counter}.')
        counter = 0
        break
