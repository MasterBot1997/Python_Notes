from logg import logging
from function import *
from check_list import *
# import csv
# import os, fnmatch

temp_num = [0]

def menu():
    num_type = ""
    logging.info("Программа запущенна.")
    print("Добро пожаловать в заметки!")
    while (num_type != "stop"):
        # список в котором на каждый цикл работы программы будут сохраняться актуальные имена файлов
        all_name_file = save_name_notes()
        checking_for_files(all_name_file)
        num_type = input("\nВыберете что вы хотите сделать:\n"
                          "1 - работа с файлами\n"
                          "2 - Создать новый файл\n"
                          "3 - Удалить файл\n"
                          "stop - завершить работу\n")
        match num_type:
                case "1":
                    print("Список файлов: ")
                    print_list_file(all_name_file)
                    command = input("Введите номер файла : ")
                    command = check_command(command,len(all_name_file))
                    logging.info(f"Начата работа с файлом {all_name_file[command-1]}")
                    menu_function(all_name_file[command-1])
                case "2":
                    name_new_file = input('Введите имя нового файла без расширения: ')
                    new_file(name_new_file)
                    logging.info(f"Создан новый файл заметок {name_new_file}.csv")
                case "3":
                    print_list_file(all_name_file)
                    command = input("Введите номер файла который хотите удалить: ")
                    command = check_command(command,len(all_name_file))
                    logging.info(f"Удаление файла {all_name_file[command-1]}")
                    delite_file(all_name_file[command-1])
                case "stop":
                    logging.info("Завершение программы.")
                    print("\nСпасибо, что пользуетесm нашим приложением!\nХорошего вам дня!")
                case _:
                    logging.warning("Пользователь ввел некоректное значение!")
                    print("Такого варанта нет, попробуйте еще раз!")
                    continue
            
    
    

def menu_function(name):
    while True:
        id_last = last_id(name)
        if id_last < temp_num[0]:
            id_last = temp_num[0]
        # Выбор пользователя какой действие он хочет выполнить
        num_type = input("\nEnter\n" 
                         "1 - Распечатать заметки\n"
                         "2 - Найти записи\n"
                         "3 - Добавить записи\n"
                         "4 - Редактировать записи\n"
                         "5 - Удалить записи\n"
                         "0 - Вернуться к выбору файла\n")
        match num_type:
            case "1":
                # Вывод всех записей в консоль
                print_file(name)
            case "2":
                # Переход в интерфейс поиска записи
                prin_dict_menu(name)
            case "3":
                # Добавление новой заметки в файл
                new_entry(id_last, name)
            case "4":
                # Переход в меню редактирования данных
                red_menu(name)
            case "5":
                # Удаление заметки по индексу
                temp_num.insert(0, id_last)
                delite_data(name)
            case "0":
                logging.info("Возвращение к выбору файла")
                print("\nВы вернулись в меню выбора файла")
                break
            case _:
                logging.warning("Пользователь ввел некоректное значение!")
                print("Такого варанта нет, попробуйте еще раз!")
                continue


# Меню печати заметок по выбранному фильтру
def prin_dict_menu(name_f):
    while True:
        # Пользователь выбирает по какому критерию хочет вывести найти и вывести заметки
        name_key = input("Ввдеите по какому параетру вы хотите вывести иформацию: \n"
                        "1 - id\n"
                        "2 - Заголовок\n"
                        "0 - Вернуться в меню\n")
        match name_key:
            case '1':
                key_user = input("Введите id заметки: ")
                print()
                filter_user = "id"
                prin_dict(filter_user, key_user, name_f)
                break
            case '2':
                key_user = input("Введите Заголовок заметки: ")
                print()
                filter_user = "header"
                prin_dict(filter_user, key_user, name_f)
                break
            case '0':
                logging.info("Возвращение в меню")
                print("\nВы возвращаетесь в меню\n")
                break
            case _:
                logging.warning("Пользователь ввел некоректное значение!")
                print("Такого варанта нет, попробуйте еще раз!")
                continue

# Меню редактирования заметок
def red_menu(name_f):
        while True:
            # Пользователь выбирает какую информацию он хочет отредактировать
            name_red = input("Ввдеите по какому параетру вы хотите изменить информацию: \n"
                            "1 - Заголовок\n"
                            "2 - Текст заметки\n"
                            "0 - Вернуться в меню\n")
            match name_red:
                case '1':
                    name_red = 1
                    redactor_data(name_red, name_f)
                    break
                case '2':
                    name_red = 2
                    redactor_data(name_red, name_f)
                    break
                case '0':
                    logging.info("Возвращение в меню")
                    print("\nВы возвращаетесь в меню\n")
                    break
                case _:
                    logging.warning("Пользователь ввел некоректное значение!")
                    print("Такого варанта нет, попробуйте еще раз!")
                    continue