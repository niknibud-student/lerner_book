""" Простая игра 'Угадай число'

    Случайно выбирается число и предлагается пользователю его угадать
"""

import random


def guessing_game() -> None:
    """ Функция игры
    """
    print('Игра "Угадай число"')
    print('Число загадывается в диапазоне от 0 до 100')
    name = input('Введите своё имя: ')
    print(f'Привет {name}!')
    secret_number = random.randint(0, 100)
    while True:
        try:
            answer_user = int(input("Отгадай число: "))
        except ValueError:
            print('Ошибка ввода! Вводить можно только числа!')
            print('Попробуйте еще раз!')

        if answer_user == secret_number:
            print('Поздравляю! Вы угадали число!')
            break

        if answer_user > secret_number:
            print('Число слишком большое!')
        else:
            print('Число слишком маленькое!')

if __name__ == '__main__':
    guessing_game()
