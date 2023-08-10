
from controller.controllerNote import SearchNotes, WriterNotes, ShowNotes
from model.model import Note


class Run:
    def search_menu():
        userValue = []
        work = True
        search_flag = True
        while work:
            answer_search = input("\nПоиск:\n"
                                  "1. Индекс\n"
                                  "2. Заголовок\n"
                                  "3. Текст (или слово)\n"
                                  "4. Выход в основное меню\n")
            match answer_search:
                case '1':
                    index_flag = True
                    search_index = 0
                    while index_flag:
                        userValue = input("Введите индекс:\n")
                        if not userValue.isdigit():
                            print("Введите число!\n")
                        else:
                            index_flag = False
                    if search_flag == SearchNotes.search_records(userValue, search_index, search_flag):
                        print("\nЗаметок с индексом " +
                              userValue + " не найдено\n")
                case '2':
                    search_index = 1
                    userValue = input(
                        "Введите заголовок (целиком или одно слово):\n")

                    if search_flag == SearchNotes.search_records(userValue, search_index, search_flag):
                        print("\nЗаметок с заголовком " +
                              userValue + " не найдено")
                case '3':
                    search_index = 2
                    userValue = input(
                        "Введите текст (целиком или одно слово):\n")

                    if search_flag == SearchNotes.search_records(userValue, search_index, search_flag):
                        print("\nЗаметок с текстом " +
                              userValue + " не найдено")
                case '4':
                    work = False
                case _:
                    print("Повторите ввод параметра поиска заметки!\n")

    def delete_menu():
        answer_delete = input("Удаление:\n"
                              "1. Индекс\n"
                              "2. Заголовок\n")
        match answer_delete:
            case '1':
                search_index = 0
                userValue = input("\nВведите индекс:\n")
                WriterNotes.delete_records(userValue, search_index)
            case '2':
                search_index = 1
                userValue = input(
                    "\nВведите заголовок (целиком или одно слово): \n")
                WriterNotes.delete_records(userValue, search_index)
            case _:
                print("\nПовторите ввод параметра удаления заметки!\n")

    def change_menu():
        answer_change = input('Замена:\n'
                              '1. Заголовок\n'
                              '2. Текст заметки\n')
        match answer_change:
            case '1':
                search_index = 1
                userValue = input(
                    "\nВведите заголовок (целиком или одно слово): \n")
                WriterNotes.change_records(
                    userValue, search_index, Note.name_note())
            case '2':
                search_index = 2
                userValue = input(
                    "\nВведите часть текста заметки (или одно слово): \n")
                WriterNotes.change_records(
                    userValue, search_index, Note.text_note())
            case _:
                print("\nПовторите ввод параметра для изменения заметки!\n")

    def main_menu(search_menu, change_menu, delete_menu):

        ShowNotes.read_records()
        work = True
        while work:
            answer = input("Заметки:\n"
                           "1. Показать все записи\n"
                           "2. Создать заметку\n"
                           "3. Поиск\n"
                           "4. Редактировать заметку\n"
                           "5. Удалить заметку\n"
                           "6. Выход\n\n")

            match answer:
                case "1":
                    print("")
                    number_of_rows = ShowNotes.show_all_records()
                    
                    print(f'Всего в файле {number_of_rows[0]} заметок.\n')
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
                    print("\nПовторите команду\n")
    main_menu(search_menu, change_menu, delete_menu)
