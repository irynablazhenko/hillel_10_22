"""
Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number является
степенью двойки, иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.

Пример:

is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256

is_power_of_two(125) # 'no' потому что это не степень двойки"""
# ____________________________________________________________________________________________________________
while True:
    try:
        number = int(input('Введите целое число : '))
        break
    except ValueError as e:
        print(f'Число не целое, ошибка: {e}')
print(f'Число {number}')

def is_power_of_two(number):
    if (number == 1):
        return 1
    elif (number > 1 and number < 2):
        return 0
    else:
        return is_power_of_two(number / 2)

if (is_power_of_two(number) == 1):
   print("Yes")
else:
    print("No")

