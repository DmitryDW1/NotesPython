
from os import path
import pandas as pd
import csv
import datetime

file_base = 'notes.csv'
temp_file_base = 'temp_file_base.txt'
file_log_csv = 'log.csv'
file_test_export = 'test.txt'
all_data = []
last_id = 0
if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        
        str = 'ID;Заголовок;Текст;Дата создания(изменения)'
        _.write(str +"\n")
        pass



def name_note():
    return input('Введите заголовок заметки: ')

def text_note():
    return input('Введите текст: ')
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