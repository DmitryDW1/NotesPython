
import os
import csv
import datetime

file_base = 'notes.csv'
temp_file_base = 'temp_file_base.csv'
file_log_csv = 'log.csv'
last_id = 0
if not os.path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def name_note():
    return input('Введите заголовок заметки: ')

def text_note():
    return input('Введите текст: ')
  

