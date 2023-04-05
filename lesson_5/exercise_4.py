"""Задание 4.
Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от
1 до n (включая n).
Реализовать в 2-х вариантах: используя цикл while и цикл for."""

n = int(input('Введите целое число: '))


total_for: int = 0
for i in range(1, n+1):
    num = i**3
    total_for += num
print(f'Сумма кубов с использованием цикла for: {total_for}')

# реализация с использованием цикла while
counter_while: int = 0
total_while: int = 0
while counter_while < n:
    counter_while += 1
    total_while += counter_while**3
print(f'Сумма кубов с использованием цикла while: {total_while}')
