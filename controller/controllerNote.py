import csv
import datetime
import os
from model.model import Note

file_base = 'notes.csv'
temp_file_base = 'temp_file_base.csv'
file_log_csv = 'log.csv'
last_id = 0
index_template = []

if not os.path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


class ShowNotes(object):
    def show_all_records():
        global last_id
        count = 0
        with open(file_base, encoding="utf-8") as f:
            file_reader = csv.reader(f, delimiter=";")
            for row in file_reader:
                Note.to_string_yellow(row)
                last_id = int(row[0])
                count += 1
            return count, last_id
    def show_all_records_date(search_date):
        global last_id
        count = 0
        with open(file_base, encoding="utf-8") as f:
            file_reader = csv.reader(f, delimiter=";")
            for row in file_reader:
                if search_date in row[3]:
                    Note.to_string_green(row)
                    last_id = int(row[0])
                    count += 1
            return count, last_id

    def read_records():
        global last_id
        global index_template
        with open(file_base) as f:
            file_reader = csv.reader(f, delimiter=";")
            if os.stat(file_base).st_size > 0:
                for row in file_reader:
                    index_template.append(row[0])
                    pass
                last_row = row
                last_id = int(last_row[0])
            return last_id, index_template


class WriterNotes(object):
    def add_records():
        global last_id
        with open(file_base, 'a', encoding="utf-8") as f:
            file_writer = csv.writer(f, delimiter=";", lineterminator="\r")
            last_id += 1
            file_writer.writerow([last_id, Note.name_note(), Note.text_note(
            ), datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")])
            return last_id

    def delete_records(userValue, del_index, search_flag):
        with open(file_base, 'r+', encoding="utf-8") as f1, open(temp_file_base, 'w', encoding="utf-8") as f2:
            rows1 = csv.reader(f1, delimiter=";")
            rows2 = csv.writer(f2, delimiter=";", lineterminator="\r")
            for row in rows1:
                if userValue not in row[del_index]:
                    rows2.writerow(row)
                    search_flag = False
                
        with open(file_base, 'w', encoding="utf-8") as f1, open(temp_file_base, 'r', encoding="utf-8") as f2:
            rows2 = csv.reader(f2, delimiter=";")
            rows1 = csv.writer(f1, delimiter=";", lineterminator="\r")
            for row in rows2:
                rows1.writerow(row)
        return search_flag

    def change_records(change_index, changes_in_note, index_id):
        with open(file_base, 'r+', encoding="utf-8") as f1, open(temp_file_base, 'w', encoding="utf-8") as f2:
            rows1 = csv.reader(f1, delimiter=";")
            rows2 = csv.writer(f2, delimiter=";", lineterminator="\r")
            flag = True
            for row in rows1:
                if index_id == row[0]:
                    row[change_index] = changes_in_note
                    row[3] = datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
                    flag = False
                rows2.writerow(row)
            if (flag):
                print("Такой заметки не найдено\n")
            else:
                print("Заметка изменена\n")
        with open(file_base, 'w', encoding="utf-8") as f1, open(temp_file_base, 'r', encoding="utf-8") as f2:
            rows2 = csv.reader(f2, delimiter=";")
            rows1 = csv.writer(f1, delimiter=";", lineterminator="\r")
            for row in rows2:
                rows1.writerow(row)


class SearchNotes(object):
    def search_records(userValue, search_index, search_flag):
        with open(file_base, 'r', encoding="utf-8") as f:
            file_reader = csv.reader(f, delimiter=";")
            if userValue.isdigit():
                for row in file_reader:
                    if userValue == row[search_index]:
                        search_flag = False
                        Note.to_string_green(row)
            else:
                for row in file_reader:
                    if userValue in row[search_index].lower():
                        search_flag = False
                        Note.to_string_green(row)
            return search_flag
