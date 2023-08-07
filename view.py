
from notesPython import *
from rwNotes import *

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
                    search_records()
                case "4":
                    change_records()
                case "5":
                    delete_records()
                case "6":
                    work = False
                case _:
                    print("Повторите команду\n")
    main_menu()