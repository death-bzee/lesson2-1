def phonebook():
    choise = show_menu()
    phonebook = read_file('phonebook.txt')
    

def show_menu():
    print("\nВыберите пункт меню для работы со справочником\n"
          "1.\n" 
          "2.\n"
          "3.\n"
          "4.\n"
          "5.\n"
          "6.")
    choise = int(input())
    return choise


def read_file(filename):
    phonebook = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phone_read:
        for line in phone_read:
            record = dict(zip(fields, line.split('')))
            phonebook.append(record)
    return phonebook


def write_file(filename, phonebook):
    s = ''
    with open(filename, 'w') as phone_write:
        for i in range(len(phonebook)):
            for v in phonebook[i].values():
                s = s + v + ','
            phone_write.write(f'{s[:-1]}\n')


def copy_line(in_file, out_file):
    print("Введите номер строки:")
    try:
        line_num = int(input()) + 1
    except:
        'Введите число'
    try:
        with open(in_file, 'r', encoding='utf-8') as file_read:
            lines = file_read.readlines()
            
            if 0 <= line_num < len(lines):
                line_to_copy = lines[line_num]
                with open(out_file, 'a', encoding='utf-8') as f_target:
                    f_target.write(line_to_copy)
                print(f"Строка номер {line_num + 1} успешно добавлена в файл {target_file}")
            else:
                print("Неверный номер строки. Выберите число между 1 и {len(lines)}")
    except:
        "Не найдены файлы"

if __name__ == "__main__":
    phonebook()