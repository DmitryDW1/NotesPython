from notesPython import *

class ShowNotes(object):
    def show_all_records():
        global last_id
        with open(file_base, encoding="utf-8") as f:
            file_reader = csv.reader(f, delimiter=";")
            count = 0 
            for row in file_reader:
                print(f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n')
                last_id = int(row[0])
                count +=1
            print(f'Всего в файле {count} заметок.')
            return last_id
        
    def read_records():
        global last_id
        with open(file_base) as f:
            file_reader = csv.reader(f, delimiter=";")
            if os.stat(file_base).st_size > 0:
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
    
    def delete_records(userValue, del_index):                                
        with open(file_base, 'r+', encoding="utf-8") as f1, open(temp_file_base, 'w', encoding="utf-8") as f2:
                    rows1 = csv.reader(f1, delimiter=";")
                    rows2 = csv.writer(f2, delimiter = ";", lineterminator="\r")
                    for row in rows1:
                        if userValue not in row[del_index]:
                            rows2.writerow(row)
        with open(file_base, 'w', encoding="utf-8") as f1, open(temp_file_base, 'r', encoding="utf-8") as f2:
            rows2 = csv.reader(f2, delimiter=";")
            rows1 = csv.writer(f1, delimiter = ";", lineterminator="\r")
            for row in rows2:
                rows1.writerow(row)
class SearchNotes(object):
    def search_records(userValue, search_index):
        with open(file_base, 'r', encoding="utf-8") as f:
            bool = True
            file_reader = csv.reader(f, delimiter=";")
            for row in file_reader:
                if userValue in row[search_index]:
                    bool = False
                    print('\n' + f'{row[0]} {row[1]} {row[2]} {row[3]}' + '\n')
            if bool:
                print("\nЗаметок не найдено\n")

    def change_records(userValue, change_index, changes_in_note):
        with open(file_base, 'r+', encoding="utf-8") as f1, open(temp_file_base, 'w', encoding="utf-8") as f2:
                    rows1 = csv.reader(f1, delimiter=";")
                    rows2 = csv.writer(f2, delimiter = ";", lineterminator="\r")
                    for row in rows1:
                        if userValue in row[change_index]:
                            old_data = row[change_index]
                            new_data = old_data.replace(userValue, changes_in_note)
                            for column in row:
                                if column != userValue:
                                    
                                    rows2.writerows(column)
                                else:
                                    rows2.writerow(new_data)
                        else: rows2.writerow(row)
                # case '2':
                #     lines1 = f1.readlines()
                #     change_phone_number_user = phone_number_user()
                #     for line in lines1:
                #         if change_phone_number_user in line:
                #             old_data = line
                #             new_data = old_data.replace(change_phone_number_user, phone_number_user())
                #             f2.write(new_data)
                #         else: f2.write(line)
                # case _:
                #     print("Try again!\n")
        # with open(file_base, 'w', encoding="utf-8") as f1, open(temp_file_base, 'r', encoding="utf-8") as f2:
        #     rows2 = csv.reader(f2, delimiter=";")
        #     rows1 = csv.writer(f1, delimiter = ";", lineterminator="\r")
        #     for row in rows2:
        #         rows1.writerow(row)
