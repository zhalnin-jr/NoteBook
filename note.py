import json 
import datetime

def print_menu():
    print("""
    ------------------------------------------------------------- \n
    Добро пожаловать в "Заметки"! \n
    Ниже представлен функционал программы. \n
    Впишите в терминал цифру для работы с соответвующей функцией! \n
    1 - Добавить заметку\n 
    2 - Вывести все заметки\n  
    3 - Найти и отредактировать заметку\n 
    4 - Удалить заметку\n 
    5 - Выход\n  
    ----------------------------------------------------------- \n 
    """)

def read_notes():
    try:
        with open('notes.json', 'r', encoding='utf8') as open_book:
            notes = json.load(open_book)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(file_path, 'w', encoding='utf8') as open_book:
        json.dump(notes, open_book, indent=4)

def add_note():
    title = (input('Введите заголовок заметки: ').title())
    body = (input('Введите текст заметки: ').title())
    idd = search_free_id()
    datatime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {'id': idd, 'title': title, 'body': body, 'datatime': datatime}
    notes.append(note)
    save_notes(notes)
    print('Заметка добавлена!')

def search_free_id():
    id_new = 1
    count = 2
    for note in notes:
        if (count != note['id']):
            id_new = count
        count += 1
    return id_new

def edit_note_id():
    note_id = int(input('Введите ID заметки для редактирования: '))
    for note in notes:
        if note['id'] == note_id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            note['title'] = title
            note['body'] = body
            note['datatime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print('Заметка отредактирована!')
            break
    else:
        print('Заметка с таким ID не найдена. Попробуйте снова!')
        edit_note_id()

def edit_note_title():
    note_title = input('Введите заголовок заметки для редактирования: ')
    for note in notes:
        if note['title'] == note_title:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            note['title'] = title
            note['body'] = body
            note['datatime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print('Заметка отредактирована!')
            break
    else:
        print('Заметка с таким заголовком не найдена. Попробуйте снова!')
        edit_note_title()

def edit_note():
    print("""
        \n Вы хотите найти заметку по id или заголовку?\n 
        1 - По id
        2 - По заголовку
        """)
    task = (int(input('Введите номер задачи: ')))
    if task == 1:
        edit_note_id()
    elif task == 2:
        edit_note_title
    else:
        print("Вы ошиблись!")
        edit_note()

def show_notes():
    for note in notes:
        print(f' {note["id"]}. {note["title"]} \n', end='')
        print(f' {note["body"]}\n', end='')
        print(f' {note["datatime"]}\n')

def delete_note():
    note_id = int(input('Введите id заметки для удаления: '))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка удалена.')
            break
    else:
        print('Заметка с таким id не найдена.')
        delete_note()

def tasks(task):
   if task > 5: 
       print('Вы ошиблись!')
       tasks(int(input('Введите номер задачи от 1 до 5: ')))
   elif task == 5: print('До свидания!')
   else:
    match task:
        case 1: ## Добавить заметку
            add_note()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 5: ')))   
        case 2: ## Вывести все заметки
            show_notes()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 5: ')))
        case 3: ## Найти и отредактировать заметку
            edit_note()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 5: ')))
        case 4: ## Удалить заметку
            delete_note()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 5: ')))

file_path = "notebook.json"
notes = read_notes()
print_menu()
tasks(int(input('Введите номер задачи от 1 до 5: ')))