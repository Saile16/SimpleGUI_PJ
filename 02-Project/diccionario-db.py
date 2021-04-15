# tenemos que instalar mysql connector
import mysql.connector
# esta coneccion esta hecha con una db del profesor del curso
# con = mysql.connector.connect(
#     user="ardit700_student",
#     password="ardit700_student",
#     host="108.167.140.122",
#     database="ardit700_pm1database"
# )
# llamaos al cursor
cursor = con.cursor()
word = input("Enter a word: ")
# hacemos un query a la base de datos
query = cursor.execute(f"SELECT * FROM Dictionary Where Expression = '{word}'")
# y aqui tenemos los resultados
results = cursor.fetchall()

if results:
    for result in results:
        print("-", result[1])
else:
    print("No wourd found")
