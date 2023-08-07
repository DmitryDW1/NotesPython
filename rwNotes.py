from notesPython import *

class ShowNotes(object):
    def show_all_records(): # Не работает last_id:( Как допилить??? Решено!
        global last_id
        with open(file_base, encoding="utf-8") as f:
            file_reader = csv.reader(f, delimiter=";")
            count = 0 
            for row in file_reader:
                if count == 0:
                    print(f'{" ".join(row)}')
                else:
                    print(f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n')
                    last_id = int(row[0])
                count +=1
            print(f'Всего в файле {count-1} строк.')
            return last_id
        
    def read_records():
        global last_id
        with open(file_base) as f:
            file_reader = csv.reader(f, delimiter=";")
            for row in file_reader:
                pass
            last_row = row
            last_id = int(last_row[0])
            return last_id

class WriterNotes(object):
    def add_records():
        global last_id
        with open(file_base, 'a', encoding="utf-8") as f:
            file_writer = csv.writer(f, delimiter = ";", lineterminator="\r")
            last_id += 1
            file_writer.writerow([last_id, name_note(), text_note(), datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")])
            return last_id
    
    def 