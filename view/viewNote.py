
from controller.controllerNote import SearchNotes, WriterNotes, ShowNotes, index_template
from model.model import Note


class Run:
    def search_menu():
        userValue = []
        search_flag = True
        global search_index
        answer_search = input("\nПоиск:\n"
                                "1. Индекс\n"
                                "2. Заголовок\n"
                                "3. Текст (или слово)\n"
                                "4. Выход в основное меню\n")
        match answer_search:
            case '1':
                digit_flag = True
                search_index = 0
                while digit_flag:
                    userValue = input("Введите индекс:\n")
                    if not userValue.isdigit():
                        print("Введите число!\n")
                    else:
                        digit_flag = False
                if search_flag == SearchNotes.search_records(userValue, search_index, search_flag):
                    print("\nЗаметок с индексом " +
                            userValue + " не найдено\n")
            case '2':
                search_index = 1
                userValue = input("Введите заголовок (целиком или одно слово):\n").lower()
                if search_flag == SearchNotes.search_records(userValue, search_index, search_flag):
                    print("\nЗаметок с заголовком " + userValue + " не найдено")
            case '3':
                search_index = 2
                userValue = input("Введите текст (целиком или одно слово):\n").lower()
                if search_flag == SearchNotes.search_records(userValue, search_index, search_flag):
                    print("\nЗаметок с текстом " + userValue + " не найдено")
            case _:
                print("Повторите ввод параметра поиска заметки!\n")

    def delete_menu():
        userValue = []
        search_flag = True
        global search_index
        answer_delete = input("Удаление:\n"
                            "1. Индекс\n"
                            "2. Заголовок\n"
                            "3. Текст (или слово)\n"
                            "4. Выход в основное меню\n")
        match answer_delete:
            case '1':
                digit_flag = True
                search_index = 0
                while digit_flag:
                    userValue = input("Введите индекс:\n")
                    if not userValue.isdigit():
                        print("Введите число!\n")
                    else:
                        digit_flag = False
                if search_flag == WriterNotes.delete_records(userValue, search_index, search_flag):
                    print("\nЗаметок с индексом " +
                            userValue + " не найдено\n")
            case '2':
                search_index = 1
                userValue = input("Введите заголовок (целиком или одно слово):\n").lower()
                if search_flag == WriterNotes.delete_records(userValue, search_index, search_flag):
                    print("\nЗаметок с заголовком " + userValue + " не найдено")
            case '3':
                search_index = 2
                userValue = input("Введите текст (целиком или одно слово):\n").lower()
                if search_flag == WriterNotes.delete_records(userValue, search_index, search_flag):
                    print("\nЗаметок с текстом " + userValue + " не найдено")
            case _:
                print("\nПовторите ввод параметра удаления заметки!\n")

    def change_menu():
        index_id = input("Введите индекс заметки:\n")
        if index_id in index_template:
            answer_change = input('Замена:\n'
                                '1. Заголовок\n'
                                '2. Текст заметки\n')
            match answer_change:
                case '1':
                    change_index = 1
                    WriterNotes.change_records(change_index, Note.name_note(), index_id)
                case '2':
                    change_index = 2
                    WriterNotes.change_records(change_index, Note.text_note(), index_id)
                case _:
                    print("\nПовторите ввод параметра для изменения заметки!\n")
        else:
            print("Заметки с таким индексом не найдено\n")

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
                    number_of_rows = "0"
                    print("")
                    answer_filter = input("Выберите режим фильтрации:\n"
                                        "1. Фильтрация по дате создания/изменения\n"
                                        "2. Фильтрация по индексу\n")
                    match answer_filter:
                        case "1":
                            search_date = input("Введите дату в формате дд/мм/гггг:\n")
                            number_of_rows = ShowNotes.show_all_records_date(search_date)
                            print(f'Всего в файле {number_of_rows[0]} заметок.\n')
                case "2":
                    WriterNotes.add_records()
                    print("\nЗаметка создана\n")
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
