class Note:

    def name_note():
        return input('Введите заголовок заметки: ')

    def text_note():
        return input('Введите текст: ')

    def to_string(row):
        print(f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n')
