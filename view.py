
from notesPython import *
from rwNotes import *
userValue = []

def search_menu():
    work = True
    while work:
        answer_search = input("\nПоиск:\n"
                    "1. Индекс\n"
                    "2. Заголовок\n"
                    "3. Выход в основное меню\n")
        match answer_search:
            case '1':
                search_index = 0
                userValue = input("\nВведите индекс: ")
                SearchNotes.search_records(userValue, search_index)
            case '2':
                search_index = 1
                userValue = input("\nВведите заголовок (целиком или одно слово): ")
                SearchNotes.search_records(userValue, search_index)
            case '3':
                work = False
            case _:
                print("\nПовторите ввод параметра поиска заметки!\n")
        
def delete_menu():
    answer_delete = input("Удаление:\n"
            "1. Индекс\n"
            "2. Заголовок\n")
    match answer_delete:
        case '1':
            search_index = 0
            userValue = input("Введите индекс: ")
            WriterNotes.delete_records(userValue, search_index)
        case '2':
            search_index = 1
            userValue = input("Введите заголовок (целиком или одно слово): \n")
            WriterNotes.delete_records(userValue, search_index)
        case _:
            print("Повторите ввод параметра удаления заметки!\n")

def change_menu():
    answer_change = input('Замена:\n'
                '1. Заголовок\n'
                '2. Текст заметки\n')
    match answer_change:
        case '1':
                search_index = 1
                userValue = input("Введите заголовок (целиком или одно слово): \n")
                SearchNotes.change_records(userValue, search_index, name_note())
        case '2':
                search_index = 2
                userValue = input("Введите часть текста заметки (или одно слово): \n")
                SearchNotes.change_records(userValue, search_index, text_note())
        case _:
                print("\nПовторите ввод параметра для изменения заметки!\n") 

def main_menu ():
    ShowNotes.read_records()
    work = True
    while work:
        answer = input("\nЗаметки:\n"
                    "1. Показать все записи\n"
                    "2. Создать заметку\n"
                    "3. Поиск\n"
                    "4. Редактировать заметку\n"
                    "5. Удалить заметку\n"
                    "6. Exit\n")
        match answer:
            case "1":
                ShowNotes.show_all_records()
            case "2":
                WriterNotes.add_records()
            case "3":
                search_menu()
            case "4":
                change_menu()
            case "5":
                delete_menu()
            case "6":
                work = False
            case _:
                print("Повторите команду\n")
main_menu()


