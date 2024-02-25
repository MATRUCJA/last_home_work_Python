my_dict = []
with open('phone_numbers.txt','r') as file:
    for i in file:
        my_list=i.split()
        my_dict.append({'Имя':my_list[0], 'Телефон':my_list[1], 'Комментарий':my_list[2]})


print("""Выберите нужный пункт меню: 
1. Показывать все контакты
2. Добавлять контакт
3. Найти контакт
4. Изменять контакт
5. Удалить контакт
6. Выход из программы""")

while True:
    try:
        menu_item=int(input())
        break
    except ValueError:
        print("Вы ввели неверное значение. Выберите пункт из меню")
        next


def show_all():
    print("Телефонный справочник")
    with open('phone_numbers.txt','r') as file:
        for i in file:
            print(i)

def write_file(my_dict):
    with open('phone_numbers.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]} {i["Телефон"]} {i["Комментарий"]}\n')

def add_contact(my_dict):
    name=input("Введите имя:\n")
    phone=input("Введите номер телефона:\n")
    comment=input("Введите комментарий:\n")
    new_string=f'{name} {phone} {comment}'
    my_dict.append({'Имя':name, 'Телефон':phone, 'Комментарий':comment})
    write_file(my_dict)

def find_contact(my_dict):
    search_word=input("Введите текст для поиска контакта:\n")
    search_result=[]
    for item in range(len(my_dict)):
        for i in my_dict[item].values():
            if search_word in i:
                print(my_dict[item])
                search_result.append(item)
    print(search_result)
    return search_result

def change_contact(my_dict,index):
    fields=list(my_dict[0].keys())
    #print(fields)
    temp_dict=my_dict[index]
    to_change=int(input("В какое поле вносим изменения: 1. Имя 2. Телефон 3. Комментарий: "))
    new_value=input("Введите новое значение поля: ")
    temp_dict[fields[to_change-1]]=new_value
    my_dict[index]=temp_dict
    write_file(my_dict)

def del_contact(my_dict, index):
    my_dict.pop(index)
    with open('phone_numbers.txt', 'w') as file:
        write_file(my_dict)


if menu_item == 1:
    show_all()
elif menu_item == 2:
    add_contact(my_dict)
elif menu_item == 3:
    find_contact(my_dict)
elif menu_item == 4:
    find_contact(my_dict)
    index = int(input("Введите номер записи из предоставленных, которую хотите изменить:" ))
    change_contact(my_dict, index)
elif menu_item == 5:
    find_contact(my_dict)
    index = int(input("Введите номер записи из представленных, которую хотите удалить:" ))
    del_contact(my_dict, index)
else: 
    exit
