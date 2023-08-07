'''
Задача №49. Общее обсуждение
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''

from os import path
import pandas as pd

file_base = 'base.txt'
temp_file_base = 'temp_file_base.txt'
file_log_csv = 'log.csv'
file_test_export = 'test.txt'
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records(): # Не работает last_id:( Как допилить??? Решено!
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
        return []

def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty base!\n")

def family_user():
    return input('Введите Фамилию: ')

def first_name_user():
    return input('Введите Имя: ')

def last_name_user():
    return input('Введите отчество: ')

def phone_number_user():
    return input('Введите номер телефона: ')

def add_records():
    global last_id
    with open(file_base, 'a', encoding="utf-8") as f:
        last_id += 1
        new_user = (f'{last_id} {family_user()} {first_name_user()} '
                    f'{last_name_user()} {phone_number_user()}\n')
        f.write(new_user)

def search_records():
    with open(file_base, 'r', encoding="utf-8") as f:
        answer_search = input('Поиск:\n'
                              '1. Фамилия\n'
                              '2. Номер телефона\n')
        match answer_search:
            case '1':
                searching_family_user = family_user()
                for line in f:
                    if searching_family_user in line:
                        print(line)
            case '2':
                searching_phone_number = phone_number_user()
                for line in f:
                    if searching_phone_number in line:
                        print(line)
            case _:
                print("Try again!\n")

        f.readline()
           
def change_records():
    with open(file_base, 'r+', encoding="utf-8") as f1, open(temp_file_base, 'w', encoding="utf-8") as f2:
        answer_change = input('Замена:\n'
                            '1. Фамилия\n'
                            '2. Номер телефона\n')
        match answer_change:
            case '1':
                lines1 = f1.readlines()
                change_family_user = family_user()
                for line in lines1:
                    if change_family_user in line:
                        old_data = line
                        new_data = old_data.replace(change_family_user, family_user())
                        f2.write(new_data)
                    else: f2.write(line)
            case '2':
                lines1 = f1.readlines()
                change_phone_number_user = phone_number_user()
                for line in lines1:
                    if change_phone_number_user in line:
                        old_data = line
                        new_data = old_data.replace(change_phone_number_user, phone_number_user())
                        f2.write(new_data)
                    else: f2.write(line)
            case _:
                print("Try again!\n")
    with open(file_base, 'w', encoding="utf-8") as f1, open(temp_file_base, 'r', encoding="utf-8") as f2:
        lines2 = f2.readlines()
        for line in lines2:
            f1.write(line)

def delete_records():
    with open(file_base, 'r+', encoding="utf-8") as f1, open(temp_file_base, 'w', encoding="utf-8") as f2:
        answer_change = input('Удаление:\n'
                            '1. Фамилия\n'
                            '2. Номер телефона\n')
        match answer_change:
            case '1':
                lines1 = f1.readlines()
                del_family_user = family_user()
                for line in lines1:
                    if del_family_user not in line:
                        f2.write(line)
            case '2':
                lines1 = f1.readlines()
                del_phone_number_user = family_user()
                for line in lines1:
                    if del_phone_number_user not in line:
                        f2.write(line)
            case _:
                print("Try again!\n")
    with open(file_base, 'w', encoding="utf-8") as f1, open(temp_file_base, 'r', encoding="utf-8") as f2:
        lines2 = f2.readlines()
        for line in lines2:
            f1.write(line)

def import_export_records():
    answer_search = input('Импорт/Экспорт данных:\n'
                              '1. Импорт\n'
                              '2. Экспорт\n')
    match answer_search:
        case '1':
            df = pd.read_table(file_base)
            df.to_csv(file_log_csv)
        case '2':
            csv = pd.read_csv(file_log_csv)
            csv.to_string(file_test_export)
        case _:
            print("Try again!\n")

def main_menu():
    work = True
    while work:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all\n"
                       "2. Add\n"
                       "3. Search\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_records()
            case "3":
                search_records()
            case "4":
                change_records()
            case "5":
                delete_records()
            case "6":
                import_export_records()
            case "7":
                work = False
            case _:
                print("Try again!\n")


main_menu()

