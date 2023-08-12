import colorama
from colorama import Fore, Style
colorama.init()

class Note:

    def name_note():
        return input(Fore.LIGHTMAGENTA_EX + 'Введите заголовок заметки: ' + Style.RESET_ALL)
        

    def text_note():
        return input(Fore.BLUE + 'Введите текст: ' + Style.RESET_ALL)

    def to_string(row):
        print('\n' + f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n')

    def to_string_red(row):
        print('\n' + Fore.RED + f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n' + Style.RESET_ALL)
        
    def to_string_yellow(row):
        print('\n' + Fore.YELLOW + f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n' + Style.RESET_ALL)
        
    def to_string_green(row):
        print('\n' + Fore.GREEN + f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n' + Style.RESET_ALL)
