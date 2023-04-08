#Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
#Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#Программа должна выводить данные
#Программа должна сохранять данные в текстовом файле
#Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
#Использование функций. Ваша программа не должна быть линейной

#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
#Логика алгоритма для изменения:
#1. Прочитать в переменную информацию из файла.
#2. Внести нужные правки в этой информации(для этого можно вызвать поиск, чтобы понять, что конкретно меняем).
#3. Перезаписать файл через 'w'
#P.s. Для уточнения поиска редактируемого элемента можно воспользоваться функцией enumerate.
#Для нахождения индекса вхождения в массиве можно использовать .index(<вхождение>)

import functions

while True:
    print('1. Вывод справочника, 2. Добавление записи, 3. Поиск записи, 4. Перезапись, 5. Удаление записи')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        data_str = functions.get_data_worker()
        user_list, full_list = functions.select_data_person(data_str)
        num = functions.get_number()
        new_worker = functions.get_data()
        functions.change_person(user_list, full_list, num, new_worker)
    elif mode == 5:
        data_str = functions.get_data_worker()
        user_list, full_list = functions.select_data_person(data_str)
        num = functions.get_number()
        functions.delete_person(user_list, full_list, num)
    else:
        break

