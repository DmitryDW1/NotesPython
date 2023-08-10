import csv
import datetime
import os
from model.model import *

file_base = 'notes.csv'
temp_file_base = 'temp_file_base.csv'
file_log_csv = 'log.csv'
last_id = 0

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
                to_string(row)
                last_id = int(row[0])
                count +=1
            return count, last_id

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
    def change_records(userValue, change_index, changes_in_note):
        with open(file_base, 'r+', encoding="utf-8") as f1, open(temp_file_base, 'w', encoding="utf-8") as f2:
                    rows1 = csv.reader(f1, delimiter=";")
                    rows2 = csv.writer(f2, delimiter = ";", lineterminator="\r")
                    flag = True
                    for row in rows1:
                        if userValue in row[change_index]:
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
            rows1 = csv.writer(f1, delimiter = ";", lineterminator="\r")
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
                        to_string(row)
            else:
                for row in file_reader:
                    if userValue in row[search_index]:
                        search_flag = False
                        to_string(row)
            return search_flag

   
