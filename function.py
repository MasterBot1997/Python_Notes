from datetime import datetime
from check_list import *
from logg import logging
import csv
import os, fnmatch

# Реализовать консольное приложение заметки, с

def print_list_file(b):
    for i in range(len(b)):
        print(f"{i+1} - {b[i]}")

# Печать заметки
def print_file(name):
    with open("all_notes/"+name, "r", encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# функция чтением данных заметки с определенным id или по Заголовку если несколько одинаковых реализовано через словарь
def prin_dict(filter, key, name_f):
    key = check_key(filter, key)
    with open("all_notes/"+ name_f, "r", encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[filter] == key:
                print(
                    row["id"],
                    row["header"],
                    row["the_note"],
                    row["data_and_time"],
                    sep=" ; ",
                )

                # header,the_note,data_and_time


# добавлением записи в файл
def new_entry(num, name):
    row = []
    current_datetime = datetime.now()
    num = num + 1
    with open("all_notes/"+name, "a", encoding="utf8", newline="") as f:
        header = input("Введите заголовок: ")
        the_note = input("Введите текст заметки: ")
        row.append(num)
        row.append(header)
        row.append(the_note)
        row.append(current_datetime)
        writer = csv.writer(f)
        writer.writerow(row)


# редактированием
def redactor_data(filter, name_f):
    print("id не должен быть равен 0!")
    key = input("\nВведите id по которому хотите отредактировать информацию: ")
    print()
    temp = []
    key = check_delite_key(key)
    current_datetime = datetime.now()
    with open("all_notes/"+name_f, "r", encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            temp.append(row)
        with open("all_notes/"+name_f, "w", encoding="utf8", newline="") as t:
            for i in range(len(temp)):
                if key != temp[i][0]:
                    writer = csv.writer(t)
                    writer.writerow(temp[i])
                else:
                    temp[i].pop(filter)
                    temp[i].insert(filter, input('Введите новую информацию: '))
                    temp[i].pop(-1)
                    temp[i].append(current_datetime)
                    writer = csv.writer(t)
                    writer.writerow(temp[i])
    logging.info(f"Редактирование информации.")


# удалением заметок.
def delite_data(name):
    print("id не должен быть равен 0!")
    key = input("Введите id по которому хотите удалит запись: ")
    print()
    temp = []
    key = check_delite_key(key)
    with open("all_notes/"+name, "r", encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            temp.append(row)
        with open("all_notes/"+name, "w", encoding="utf8", newline="") as t:
            for i in range(len(temp)):
                if key != temp[i][0]:
                    writer = csv.writer(t)
                    writer.writerow(temp[i])
    logging.info(f"Удалена информация с id {key}")


# Оппределение последнего id
def last_id(name):
    with open("all_notes/"+name, "r", encoding="utf8") as f:
        g = f.readlines()[-1].split(",")
        c = g[0]
        b = check_last_id(c)
        return b

# Метод возвращающий все имена файлов заметок
def save_name_notes():
    all_file = []
    listOfFiles = os.listdir('all_notes/.')  
    pattern = "*.csv"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
                all_file.append(entry)
    return all_file

# Создание нового файла заметок
def new_file(name):
    row_zero = ["id","header","the_note","data_and_time"]
    with open("all_notes/"+name+".csv", "w+", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(row_zero)

# Удаление файла
def delite_file(name):
    path = "all_notes/"+name
    os.remove(path)