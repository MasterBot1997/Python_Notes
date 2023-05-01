from logg import logging
import csv
# Проверка является ли id первым или нет, на слуай нового списка
def check_last_id(num):
    if num.isdigit():
        logging.info(f"Последний id - {num}")
        return int(num)
    else:
        logging.info("Это первая заметка id - 1")
        num = 0
        return int(num)

# Проверка корректности ввода ключа, для полчучения данных о 
# пользователе через id
def check_key(filter, num):
    while True:
        with open("all_notes/text.csv", 'r',encoding='utf8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[filter] == num:
                    return num
            else:
                logging.warning("Введен несуществующий параметр")
                print("\n'Такого параметра не существует!'")
                num = input("Введите еще раз: ")
                print()

# Проверка ключа id для удаления строки с информацией
def check_delite_key(a):
    while True:
        if a.isdigit():
            if int(a) != 0:
                return a
            else:
                logging.warning("Ошбка: id = 0")
                print("\nid не должен быть равен 0!")
                a = input("Введите еще раз: ")
            print()
        else:
            logging.warning("Введен неверный  id")
            print("\nВы ввели некоректный id!")
            a = input("Введите еще раз: ")
            print()

def checking_for_files(all_file):
    if len(all_file) == 0: 
            print('Приетствую, у вас еще нет файлов с заметками.\nДавайте создадим новый!')
            name_new_file = input('Введите имя нового файла без расширения: ')
            row_zero = ["id","header","the_note","data_and_time"]
            with open("all_notes/"+name_new_file+".csv", "w+", encoding="utf8") as f:
                writer = csv.writer(f)
                writer.writerow(row_zero)
            logging.info(f"Еще нет файлов, создан новый файл заметок {name_new_file}")
    return True

def check_command(a,b):
    while True:
        if (a.isnumeric() and int(a)>0<=b):
            return int(a)
        else:            
            logging.warning("Некорректные данные!")
            print("\n'Неккоректные данные!'")
            a = input("Введите номер файла еще раз: ")
