todo=[]

def add_todo(add_new):
    todo.append(add_new)

def expand_todos(tasks):
    print("numer indeksu - nazwa zadania")
    for line in tasks:
        number=tasks.index(line)
        print(number," - ", line)

def delete_todo(tasks, number_index):
    if number_index >= 0 and number_index < len(tasks):
        tasks.pop(number_index)
    else:
        print("Podano niepoprawną wartość.")

def save_file(tasks):
    with open("todo.txt", "w", encoding="utf-8") as file_todo:
        for task in tasks:
            file_todo.write(f"{task}\n")

def load_task_from_file(tasks):
    try:
        with open("todo.txt", "r", encoding="utf-8") as todos:
            for line in todos.readlines():
                tasks.append(line.strip())
    except FileNotFoundError:
        return

load_task_from_file(todo)
while True:
    print("1:Dodaj nowe todo")
    print("2:Wyświetl listę todo")
    print("3:Usuń todo")
    print("4:Zapisz zmiany do pliku")
    print("5:wyjdź")
    option=int(input("Wybierz opcję: "))
    if option == 1:
        add_new_todo= input("Wprowadź nowe zadanie do wykonania: ")
        add_todo(add_new_todo)
    elif option == 2:
        expand_todos(todo)
    elif option == 3:
        expand_todos(todo)
        number_index= int(input("Wprowadź numer indeksu dla zadania do usunięcia: "))
        delete_todo(todo, number_index)
    elif option == 4:
        save_file(todo)
    elif option == 5:
        exit("Wychodzimy z aplikacji")
    else:
        exit("Wprowadziłeś niepoprawne dane, uruchom ponownie aplikacje.")
