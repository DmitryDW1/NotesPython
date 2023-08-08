
from notesPython import *
from rwNotes import *
userValue = []
class Run(object):
    def main_menu():
        ShowNotes.read_records()
        work = True
        while work:
            answer = input("Заметки:\n"
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
                    def search_menu():
                        answer_search = input("\nПоиск:\n"
                                    "1. Индекс\n"
                                    "2. Заголовок\n")
                        match answer_search:
                            case '1':
                                search_index = 0
                                userValue = input("\nВведите индекс: ")
                                SearchNotes.search_records(userValue, search_index)
                            case '2':
                                search_index = 1
                                userValue = input("\nВведите заголовок (целиком или одно слово): ")
                                SearchNotes.search_records(userValue, search_index)
                            case _:
                                print("\nПовторите ввод параметра поиска заметки!\n")
                    search_menu()
                case "4":
                    def change_menu():
                        answer_change = input('Замена:\n'
                                    '1. Заголовок\n'
                                    '2. \n')
                        match answer_change:
                            case '1':
                                    change_index = 1
                                    userValue = input("Введите заголовок: ")
                                    SearchNotes.change_records(userValue, change_index, name_note())
                            case '2':
                                    change_index = 2
                                    userValue = input("Введите заголовок (целиком или одно слово): \n")
                                    SearchNotes.change_records(userValue, change_index, text_note())
                            case _:
                                    print("\nПовторите ввод параметра для изменения заметки!\n")
                    change_menu()        
                case "5":
                    answer_delete = input("Удаление:\n"
                                "1. Индекс\n"
                                "2. Заголовок\n")
                    def delelete_menu():
                        match answer_delete:
                            case '1':
                                del_index = 0
                                userValue = input("Введите индекс: ")
                                WriterNotes.delete_records(userValue, del_index)
                            case '2':
                                del_index = 1
                                userValue = input("Введите заголовок (целиком или одно слово): \n")
                                WriterNotes.delete_records(userValue, del_index)
                            case _:
                                print("Повторите ввод параметра удаления заметки!\n")
                    delelete_menu()
                case "6":
                    work = False
                case _:
                    print("Повторите команду\n")
    main_menu()