import sqlite3

connection = sqlite3.connect("todo.db")

def create_table(connection):
    try:
        cur=connection.cursor()
        cur.execute("""CREATE TABLE tasks(task text)""")
    except:
        pass

def add_todo(add_new, connection):
    if add_new == "":
        print("Powrót do menu")
    else:
        cur=connection.cursor()
        cur.execute("""INSERT INTO tasks(task) VALUES(?)""", (add_new,))
        connection.commit()

def expand_todos(connection):
    cur=connection.cursor()
    cur.execute("""SELECT rowid, task FROM tasks""")
    result=cur.fetchall()
    for row in result:
        print(f'{row[0]} - {row[1]}')

def delete_todo(connection, number_index):
    cur=connection.cursor()
    row_delete=cur.execute("""DELETE FROM tasks WHERE rowid=?""", (number_index,)).rowcount
    if row_delete == 0:
        print("Takie zadanie nie istnieje.")
    else:
        print("Usunięto zadanie.")
    connection.commit()

create_table(connection)

while True:
    print("1:Dodaj nowe todo")
    print("2:Wyświetl listę todo")
    print("3:Usuń todo")
    print("4:wyjdź")
    option=int(input("Wybierz opcję: "))
    if option == 1:
        add_new_todo= input("Wprowadź nowe zadanie do wykonania: ")
        add_todo(add_new_todo, connection)
    elif option == 2:
        expand_todos(connection)
    elif option == 3:
        expand_todos(connection)
        number_index= int(input("Wprowadź numer indeksu dla zadania do usunięcia: "))
        delete_todo(connection, number_index)
    elif option == 4:
        exit("Wychodzimy z aplikacji")
    else:
        exit("Wprowadziłeś niepoprawne dane, uruchom ponownie aplikacje.")
