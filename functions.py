def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'{fio} | {tel_number}\n')

def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    print(search(tel_book, data))

def search(book: str, info: str) -> str:
    '''Находит в строке запись по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post]) # join соединяет элементы списка по указанному в начале разделителю (\n)

def get_data():
    print('Введите данные: ')
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    data_str = fio + " | " + tel_number + "\n"
    return data_str

def get_data_worker():
    data = input('Введите данные, которые хотите посмотреть: ')
    return data

def select_data_person(worker):
    user_list = []
    with open('book.txt', 'r', encoding='utf-8') as f:
        full_list = f.readlines()
        for count, line in enumerate(full_list):
            if worker in line:
                user_list.append(line)
                print(f"{count+1} {line}")
    return user_list, full_list

def get_number():
    num = int(input('Выбрать строку для изменения: '))
    return num

def delete_person(user_list, full_list, num):
    with open('book.txt', 'w', encoding='utf-8') as f:
        print(user_list, full_list, num)
        for line in full_list:
            if user_list[num-1] != line:
                f.write(line)
    print('Готово')

def change_person(user_list, full_list, num, new_worker):
    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in full_list:
            if user_list[num-1] != line:
                f.write(line)
            else:
                f.write(new_worker)
    print('Готово')