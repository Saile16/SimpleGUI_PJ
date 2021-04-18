import sqlite3

# al crear la funcion y llamarla al instante la funcion esta siendo llamada
# al momento de entrar al programa todo el tiempo


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text,year integer, isbn integer )")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):

    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


# podemos parametros por defecto en string par que se poermita la busqueda
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
# insert("The Odisea", "Andre We", 1900, 15544888)
# delete(3)
# update(4, "Odisea", "Andre L.", 1950, 55555555)
# print(view())
print(search(author="Jhon Table2"))
