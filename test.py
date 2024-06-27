fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

def phonebook_main():
    filename = 'phonebook.txt'
    phonebook = read_file(filename)
    while (True):
        choise = show_menu()

        if (choise == 1):
            print_result(phonebook)
        elif (choise == 2):
            last_name = input('Фамилия: ')
            print(find_by_lastname(phonebook, last_name))
        elif (choise == 3):
            number = input('Номер телефона: ')
            print(find_by_number(phonebook, number))
        elif (choise == 4):
            user_data = input('Введите данные через запятую: ')
            phonebook = add_user(phonebook, user_data)
            write_file(filename, phonebook)
        elif (choise == 5):
            last_name = input('Фамилия : ')
            print(delete_by_lastname(phonebook, last_name))
        elif (choise == 6):
            line = int(input('line'))
            target_file = input('target file: ')
            copy_line(filename, target_file, line)
        elif (choise == 7):
            last_name = input('Фамилия: ')
            new_number = input('Новый номер: ')
            phonebook = change_number(phonebook, last_name, new_number)
            write_file(filename, phonebook)
        elif (choise == 8):
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 8.")

def show_menu():
    print("\nВыберите пункт меню для работы со справочником\n"
          "1. Отобразить весь справочник\n" 
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Записать строку в другой файл\n"
          "7. Изменить номер телефона \n"
          "8. Выйти с программы")
    choise = int(input())
    return choise


def read_file(filename):
    phonebook = []
    with open(filename, 'r', encoding='utf-8') as phone_read:
        for line in phone_read:
            record = dict(zip(fields, line.split(',')))
            phonebook.append(record)
    return phonebook


def write_file(filename, phonebook):
    with open(filename, 'w') as phone_write:
        for i in range(len(phonebook)):
            s = ''
            for v in phonebook[i].values():
                print(v)
                s = s + v + ','
            phone_write.write(f'{s[:-1]}\n')
    

def copy_line(in_file, out_file, line_num):

   
    try:
        with open(in_file, 'r', encoding='utf-8') as file_read:
            lines = file_read.readlines()
            
            if 0 <= line_num-1 < len(lines):
                line_to_copy = lines[line_num-1]
                with open(out_file, 'a', encoding='utf-8') as f_target:
                    f_target.write(line_to_copy)
                print(f"Строка номер {line_num} успешно добавлена в файл {out_file}")
            else:
                print(f"Неверный номер строки. Выберите число между 1 и {len(lines)}")
    except:
        "Не найдены файлы"

def print_result(phonebook):
    if len(phonebook)==0:
        print('Нет записей')
    for record in phonebook:
        print(record)

def find_by_lastname(phonebook, lastname):
    for record in phonebook:
        if record['Фамилия'] == lastname:
            return record
    else:
        return 'No results'
    
def find_by_number(phonebook, phone_num):
    for record in phonebook:
        if record['Телефон'] == phone_num:
            return record
    else:
        return 'No results'

def add_user(phonebook, user_data):
    record = dict(zip(fields, user_data.split(',')))
    #print(record)
    phonebook.append(record)
    return phonebook

def delete_by_lastname(phonebook, lastname):
    phonebook = [record for record in phonebook if record['Фамилия'] != lastname]
    write_file('phonebook.txt', phonebook)
    return phonebook


def change_number(phonebook, lastname, new_number):
    print(phonebook)
    for record in phonebook:
        print(record['Фамилия'])
        if record['Фамилия'] == lastname:
            record['Телефон'] = new_number
    return phonebook

if __name__ == "__main__":
    phonebook_main()
    # phonebook = read_file('phonebook.txt')
    # user_data = 'Nashauova,Aida,87012284687,Wife'
    # record = dict(zip(fields, user_data.split(',')))
    # print(record)
    # phonebook = add_user(phonebook, user_data)
    # write_file('phonebook.txt', phonebook)
    # print(phonebook)
    # print(len(phonebook))