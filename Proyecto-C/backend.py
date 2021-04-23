import sqlite3

# import pandas
# df = pandas.read_csv('1.csv', encoding='utf-8', sep='\t',
#                      delimiter=';', skiprows=0, low_memory=False)
# # print(df)
# grupo = list(df["grupo"])
# alimento = list(df["nombre"])
# caloria = list(df["calorias"])
# proteina = list(df["proteinas"])
# carbohidratos = list(df["carbohidratos"])
# grasas = list(df["grasas"])
# fibra = list(df["fibra"])

# grupoL = []
# alimentoL = []
# for i in grupo:
#     grupoL.append(i.lower())
# for j in alimento:
#     alimentoL.append(j.lower())
# # print(grupo[0], alimento[0], caloria[0], proteina[0],
# #       carbohidratos[0], grasas[0], fibra[0])


def connect():
    conn = sqlite3.connect("alimentos.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS alimento (id INTEGER PRIMARY KEY, grupo text , alimento text,calorias integer, proteinas integer,carbohidratos integer,grasas integer,fibra integer )")
    conn.commit()
    conn.close()


def search(alimento):
    conn = sqlite3.connect("alimentos.db")
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM alimento WHERE alimento LIKE '{alimento}%'")
    rows = cur.fetchall()
    conn.close()
    return rows


# def insertar(gr, ali, cal, prot, carb, gra, fib):
#     conn = sqlite3.connect("alimentos.db")
#     cur = conn.cursor()
#     for g in zip(gr, ali, cal, prot, carb, gra, fib):
#         cur.execute(
#             "INSERT INTO alimento VALUES (NULL,?,?,?,?,?,?,?)", (g[0], g[1], g[2], g[3], g[4], g[5], g[6]))
#         conn.commit()
#     conn.close()


connect()
# insertar(grupoL, alimentoL, caloria, proteina, carbohidratos, grasas, fibra)

# print(search())
