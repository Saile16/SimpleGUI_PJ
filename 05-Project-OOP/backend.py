import sqlite3

# al crear la funcion y llamarla al instante la funcion esta siendo llamada
# al momento de entrar al programa todo el tiempo


class Database:
    # esto vendria a ser como el constructor
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text,year integer, isbn integer )")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute(
            "INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):

        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    # podemos parametros por defecto en string par que se poermita la busqueda

    def search(self, title="", author="", year="", isbn=""):

        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                         (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):

        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):

        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",
                         (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# insert("The Odisea", "Andre We", 1900, 15544888)
# delete(3)
# update(4, "Odisea", "Andre L.", 1950, 55555555)
# print(view())
# print(search(author="Jhon Table2"))
