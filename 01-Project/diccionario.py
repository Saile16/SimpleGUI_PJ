import json
# usaremos una libreria de python que permite comparar las palabras y
# devuelve un ratio de comparacion
from difflib import get_close_matches
# abrimos el json y esto lo convierte en un dict
data = json.load(open("datos.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    # de esta manera verificamos si existe alguna palabra con la primera letra como mayuscula
    # y si no existe pues volvemos a buscar en el json pero todo en minuscula
    elif word.title() in data:
        return data[word.title()]
    # ahora para acronimos como USA o NATO
    elif word.upper() in data:
        return data[word.upper()]
    # esto verifica si existe devolucion de algun dato
    elif len(get_close_matches(word, data.keys())) > 0:
        # aqui preguntamos si quiso decir la palabra con la coincidencia mas cercana [0]
        yn = input(
            f"Did you mean {get_close_matches(word,data.keys())[0]} Enter 'Y' is yes , or 'N' if no: ").lower()
        if yn == "y":
            # devolvemos el resultado de la consulta en el diccionario de esta manera
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


# pedimos el input al usuario
word_input = input("Enter a word: ")
# obtenemos el resultado de la funcion
output = translate(word_input)
# verificamos si nos devolvio una lista con definiciones de la palabra
# o un string que puede ser una deficion o que la palabra no existe
if type(output) == list:
    for item in output:
        print("-", item)
else:
    print(output)
