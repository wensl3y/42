from random import randint
from sys import exit

i = 0
while True:
    choice = input('Вычислим ответ на Главный вопрос жизни человека, Вселенной и т.д.? (y/n)')
    choice = choice.lower()
    if choice in 'y':
        while True:
            a = abs((randint(1, 10000)) * 4 / 7 + 10)
            if bool(a == 42) == True:
                i = i + 1
                print(a)
                print('Ответ получен - 42.')
                print('Получено с %d попытки.' %i)
                exit(0)
            else:
                print(a)
                print('# Повтор. #')
                print(bool(a==42))
                i = i + 1
    elif choice in 'n':
        print('До свидания.')
        break
    else:
        print('Повторите ввод.')
