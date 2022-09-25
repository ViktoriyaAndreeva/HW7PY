from telnetlib import STATUS


def menu():
    print("Приветствуем Вас в нашем телефонном справочнике!")
    print('''Меню:
    1 Добавить контакт
    2 Удалить контакт 
    3 Импортировать данные в формате 1
    4 Импортировать данные в формате 2
    5 Экспортировать данные в формате 1
    6 Экспортировать данные в формате 2
    7 Посмотреть контакты
    8 Найти контакт по фамилии
    9 Выход из справочника
      ''')
   
menu()


def control_menu():
    while True: 
        number = input('Выберите нужное действие: ')
        if number.isdigit(): 
            number = int(number)
            if number > 0 and number <= 10:
                return number
            else:
                print('Введите правильный выбор в меню')
                continue
        print('Вы ввели не цифру! Начните сначала!') 
        continue     

print(control_menu())
