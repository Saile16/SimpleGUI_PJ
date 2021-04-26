from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
import os
import backend


def get_selected_row(event):
    # try:
    #     # # PARA QUE LOS DATOS SEAN ENVIADOS globalmente y no solo en la funcion
    #     # global selected_tuple
    #     # # con esto obtenemos el index del evento

    #     # index = tabla.curselection()[0]
    #     # # aqui obtenemoos todo el valor de la tupla o lista
    #     # selected_tuple = tabla.get(index)
    #     # # con este metodo ponemos los datos al hacer click en sus casilas respectivas
    #     # e1.delete(0, END)
    #     # e1.insert(END, selected_tuple[1])
    #     # e2.delete(0, END)
    #     # e2.insert(END, selected_tuple[2])
    #     # e3.delete(0, END)
    #     # e3.insert(END, selected_tuple[3])
    #     print(selected_tuple)
    # except:
    #     pass
    # click = tabla.item(tabla.selection())
    try:
        item = tabla.selection()[0]
        lista = tabla.item(item)["values"]
        nombre = lista[1]
        calorias = lista[2]
        if calorias == "None":
            calorias = 0
        proteinas = lista[3]
        if proteinas == "None":
            proteinas = 0
        carbohidrato = lista[4]

        if carbohidrato == "None":
            carbohidrato = 0
        grasas = lista[5]
        if grasas == "None":
            grasas = 0
        fibra = lista[6]
        if fibra == "None":
            fibra = 0

        # print(lista)

        e1.delete(0, END)
        e1.insert(END, nombre)
        e2.delete(0, END)
        e2.insert(END, calorias)
        e3.delete(0, END)
        e3.insert(END, proteinas)

        e4_f1.delete(0, END)
        e4_f1.insert(END, carbohidrato)

        e5_f1.delete(0, END)
        e5_f1.insert(END, grasas)

        e6_f1.delete(0, END)
        e6_f1.insert(END, fibra)

        # print(nombre, calorias, proteinas)
    except:
        pass


def get_selected_row2(event):
    try:
        global item_t2
        item_t2 = tabla2.selection()[0]

    except:
        pass


def search_command():
    # tabla.delete(0, END)
    result = backend.search(alimento_text.get())
    registro = tabla.get_children()
    for j in registro:
        tabla.delete(j)
    for i in result:
        tabla.insert("", END, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5], i[6], i[7]))


def calcular():
    # print(type(calorias_text.get()))
    calorias = float(calorias_text.get())
    proteinas = float(proteinas_text.get())
    carbohidratos = float(carbohidrato_text.get())
    grasas = float(grasas_text.get())
    fibra = float(fibra_text.get())

    cantidad_gr = cantidad_text.get()

    calorias = calorias*cantidad_gr/100
    proteinas = proteinas*cantidad_gr/100
    carbohidratos = carbohidratos*cantidad_gr/100
    grasas = grasas*cantidad_gr/100
    fibra = fibra*cantidad_gr/100

    l5.config(text=f"TOTAL DE INGESTA DE:\n{alimento_text.get().capitalize()}")

    e5.delete(0, END)
    e5.insert(END, round(calorias, 2))
    e6.delete(0, END)
    e6.insert(END, round(proteinas, 2))

    e20_fr3.delete(0, END)
    e20_fr3.insert(END, round(carbohidratos, 2))
    e21_fr3.delete(0, END)
    e21_fr3.insert(END, round(grasas, 2))
    e22_fr3.delete(0, END)
    e22_fr3.insert(END, round(fibra, 2))


def agregar_comida():

    alimento = alimento_text.get()
    calorias = float(calorias_text_result.get())
    proteinas = float(proteinas_text_result.get())
    carbohidratos = float(carbohidrato_text_result.get())
    grasas = float(grasa_text_result.get())
    fibra = float(fibra_text_result.get())

    tabla2.insert("", END, text=1, values=(
        alimento, calorias, proteinas, carbohidratos, grasas, fibra))
    sumar_tabla2()


def sumar_tabla2():
    calorias_total = 0
    proteinas_total = 0
    carbohidratos_total = 0
    grasas_total = 0
    fibra_total = 0
    child = tabla2.get_children()
    for i in child:
        calorias_total += float(tabla2.item(i, 'values')[1])
        proteinas_total += float(tabla2.item(i, 'values')[2])
        carbohidratos_total += float(tabla2.item(i, 'values')[3])
        grasas_total += float(tabla2.item(i, 'values')[4])
        fibra_total += float(tabla2.item(i, 'values')[5])
        # print(calorias_total)
    # nuevo_cal_valor = calorias_total
    l30.config(
        text=f"DIETA\nCal: {round(calorias_total,2)} - Prot: {round(proteinas_total,2)} - Carb: {round(carbohidratos_total,2)} - Grasas: {round(grasas_total,2)} - Fib: {round(fibra_total,2)}")


def eliminar_comida():
    registro = tabla2.get_children()
    tabla2.delete(item_t2)
    sumar_tabla2()


def limpiar_dieta():
    with open("fruits.txt", "w+") as myfile:
        registro = tabla2.get_children()
        for j in registro:
            tabla2.delete(j)
            myfile.write("")
        sumar_tabla2()


def escribir_block():
    nombre = ""
    calorias_total = 0
    proteinas_total = 0
    carbohidratos_total = 0
    grasas_total = 0
    fibra_total = 0
    child = tabla2.get_children()

    with open("Dieta.txt", "w+") as myfile:
        for i in child:
            c = 0
            nombre = str(tabla2.item(i, 'values')[0])
            calorias_total = float(tabla2.item(i, 'values')[1])
            proteinas_total = float(tabla2.item(i, 'values')[2])
            carbohidratos_total = float(tabla2.item(i, 'values')[3])
            grasas_total = float(tabla2.item(i, 'values')[4])
            fibra_total = float(tabla2.item(i, 'values')[5])
            myfile.write(
                f"*{nombre}-{calorias_total}-{proteinas_total}-{carbohidratos_total}-{grasas_total}-{fibra_total}\r\n")
            # myfile.write(f"*{nombre}-Cal:{calorias_total}kcal-Prot:{proteinas_total}-Carb:{carbohidratos_total}-Grasas:{grasas_total}-Fib:{fibra_total}\r\n")
    os.startfile("Dieta.txt")


window = Tk()

window.wm_title("Titang-App")
window.geometry("1700x600")
# img = Image.open(r"logo.jpg")  # your jpeg image path
# img.save(r"Icon.ico")

imagen = PhotoImage(file="titang.png")
imagen = imagen.subsample(3)
fondo = Label(window, image=imagen).grid(
    row=0, column=0, columnspan=1)

# Aqui ira todo del frame1
frame1 = Frame(window)

frame1.grid(row=0, column=1, columnspan=2,
            rowspan=2,  ipadx=25, ipady=15, pady=42)

l1 = Label(frame1, text="Alimento")
l1.grid(row=0, column=1, ipadx=2, ipady=6)
alimento_text = StringVar()
e1 = Entry(frame1, width=30, textvariable=alimento_text)
e1.grid(row=0, column=2, ipadx=2, ipady=6)

l2 = Label(frame1, text="Calorias")
l2.grid(row=1, column=1, ipadx=2, ipady=4)
calorias_text = StringVar()
e2 = Entry(frame1, textvariable=calorias_text)
e2.grid(row=1, column=2, ipadx=2, ipady=4)

l3 = Label(frame1, text="Proteinas")
l3.grid(row=2, column=1, ipadx=2, ipady=4)
proteinas_text = StringVar()
e3 = Entry(frame1, textvariable=proteinas_text)
e3.grid(row=2, column=2, ipadx=2, ipady=4)

l4_f1 = Label(frame1, text="Carbohidratos")
l4_f1.grid(row=3, column=1, ipadx=2, ipady=4)
carbohidrato_text = StringVar()
e4_f1 = Entry(frame1, textvariable=carbohidrato_text)
e4_f1.grid(row=3, column=2, ipadx=2, ipady=4)

l5_f1 = Label(frame1, text="Grasas")
l5_f1.grid(row=4, column=1, ipadx=2, ipady=4)
grasas_text = StringVar()
e5_f1 = Entry(frame1, textvariable=grasas_text)
e5_f1.grid(row=4, column=2, ipadx=2, ipady=4)

l6_f1 = Label(frame1, text="Fibra")
l6_f1.grid(row=5, column=1, ipadx=2, ipady=4)
fibra_text = StringVar()
e6_f1 = Entry(frame1, textvariable=fibra_text)
e6_f1.grid(row=5, column=2, ipadx=2, ipady=4)

l4 = Label(frame1, text="Cantidad en gramos")
l4.grid(row=6, column=1, ipadx=2, ipady=4)
cantidad_text = DoubleVar()
e4 = Entry(frame1, textvariable=cantidad_text)
e4.grid(row=6, column=2, ipadx=2, ipady=4)

b1 = Button(frame1, text="Buscar Alimento",
            width=12, command=search_command)
b1.grid(row=0, column=3, rowspan=1, padx=7)

b2 = Button(frame1, text="Calcular", width=10, height=2, command=calcular)
b2.grid(row=2, column=3, rowspan=2)
# frame1=row=0,column=1,columspan=2,rowspan=2
# imagen=row=0, column=0, rowspan=2,columspan=1)

frame2 = Frame(window)
frame2.grid(row=3, column=0, columnspan=2, rowspan=2, pady=0)
l5 = Label(frame2, text="Resultado", font=(100))
l5.grid(row=0, column=0, columnspan=2)

tabla = ttk.Treeview(frame2)
tabla['columns'] = ("Grupo", "Nombre", "Calorias",
                    "Proteinas", "Carb", "Grasas", "Fib")
vsb = ttk.Scrollbar(window, orient="vertical", command=tabla.yview)
vsb.place(x=884, y=344, height=200+25)
tabla.configure(yscrollcommand=vsb.set)
tabla.column("#0", anchor=CENTER, width=55)
tabla.column("#1", anchor=CENTER, width=200)
tabla.column("#2", anchor=CENTER, width=225)
tabla.column("#3", anchor=CENTER, width=80)
tabla.column("#4", anchor=CENTER, width=80)
tabla.column("#5", anchor=CENTER, width=80)
tabla.column("#6", anchor=CENTER, width=80)
tabla.column("#7", anchor=CENTER, width=80)
tabla.grid(row=1, column=0, columnspan=2)
tabla.heading("#0", text="id", anchor=CENTER)
tabla.heading("#1", text="Grupo", anchor=CENTER)
tabla.heading("#2", text="Nombre", anchor=CENTER)
tabla.heading("#3", text="Calorias", anchor=CENTER)
tabla.heading("#4", text="Proteinas", anchor=CENTER)
tabla.heading("#5", text="Carb", anchor=CENTER)
tabla.heading("#6", text="Grasas", anchor=CENTER)
tabla.heading("#7", text="Fib", anchor=CENTER)
tabla.bind("<ButtonRelease-1>", get_selected_row)
# frame1=row=0,column=1,columspan=2
# imagen=row=0, column=0, rowspan=2,columspan=1)
# frame2.grid(row=3, column=0, columnspan=2)


frame3 = Frame(window)

frame3.place(x=1100, y=55)
l5 = Label(frame3, text="TOTAL DE INGESTA")
l5.grid(row=0, column=1, columnspan=2)

l1r = Label(frame3, text="Calorias")
l1r.grid(row=1, column=1, ipadx=2, ipady=4, pady=1)

calorias_text_result = StringVar()
e5 = Entry(frame3, textvariable=calorias_text_result)
e5.grid(row=1, column=2, ipadx=2, ipady=4, pady=1)

l2r = Label(frame3, text="Proteinas")
l2r.grid(row=2, column=1, ipadx=2, ipady=4, pady=1)
proteinas_text_result = StringVar()
e6 = Entry(frame3, textvariable=proteinas_text_result)
e6.grid(row=2, column=2, ipadx=2, ipady=4, pady=1)

# falta de orden crearemos labels y entry altos
l20_fr3 = Label(frame3, text="Carbohidratos")
l20_fr3.grid(row=3, column=1, ipadx=2, ipady=4, pady=1)
carbohidrato_text_result = StringVar()
e20_fr3 = Entry(frame3, textvariable=carbohidrato_text_result)
e20_fr3.grid(row=3, column=2, ipadx=2, ipady=4, pady=1)

l21_fr3 = Label(frame3, text="Grasa")
l21_fr3.grid(row=4, column=1, ipadx=2, ipady=4, pady=1)
grasa_text_result = StringVar()
e21_fr3 = Entry(frame3, textvariable=grasa_text_result)
e21_fr3.grid(row=4, column=2, ipadx=2, ipady=4, pady=1)

l22_fr3 = Label(frame3, text="Fibra")
l22_fr3.grid(row=5, column=1, ipadx=2, ipady=4, pady=1)
fibra_text_result = StringVar()
e22_fr3 = Entry(frame3, textvariable=fibra_text_result)
e22_fr3.grid(row=5, column=2, ipadx=2, ipady=4, pady=1)

b3 = Button(frame3, text="Agregar Comida", width=20,
            height=2, command=agregar_comida)
b3.grid(row=0, column=3, rowspan=3, padx=15, pady=10)
b4 = Button(frame3, text="Eliminar Comida", width=20,
            height=2, command=eliminar_comida)
b4.grid(row=4, column=3, rowspan=5, padx=15, pady=10)
# frame1=row=0,column=1,columspan=2
# imagen=row=0, column=0, rowspan=2,columspan=1)
# frame2.grid(row=3, column=0, columnspan=2)
# fram3(row=0, column=4, rowspan=2)
# font=(100)

frame4 = Frame(window)
frame4.place(x=1000, y=318)
l30 = Label(frame4, text="Dieta", font=(100))
l30.grid(row=0, column=0, columnspan=2)

tabla2 = ttk.Treeview(frame4)
tabla2['columns'] = ("Nombre", "Calorias", "Proteinas",
                     "Carb", "Grasas", "Fib")
vsb2 = ttk.Scrollbar(window, orient="vertical", command=tabla2.yview)
vsb2.place(x=1585, y=344, height=200+25)
tabla2.configure(yscrollcommand=vsb2.set)
tabla2.column("#0", anchor=CENTER, width=0, stretch=NO)
tabla2.column("#1", anchor=CENTER, width=180)
tabla2.column("#2", anchor=CENTER, width=80)
tabla2.column("#3", anchor=CENTER, width=80)
tabla2.column("#4", anchor=CENTER, width=80)
tabla2.column("#5", anchor=CENTER, width=80)
tabla2.column("#6", anchor=CENTER, width=80)
tabla2.grid(row=1, column=1)
tabla2.heading("#0", text="N°")
tabla2.heading("#1", text="Nombre", anchor=CENTER)
tabla2.heading("#2", text="Calorias", anchor=CENTER)
tabla2.heading("#3", text="Proteinas", anchor=CENTER)
tabla2.heading("#4", text="Carb", anchor=CENTER)
tabla2.heading("#5", text="Grasas", anchor=CENTER)
tabla2.heading("#6", text="Fib", anchor=CENTER)
tabla2.bind("<ButtonRelease-1>", get_selected_row2)
b1_f2 = Button(window, text="Limpiar", width=10,
               height=2, command=limpiar_dieta)
b1_f2.place(x=1598, y=480)
b2_f2 = Button(window, text="Enviar Block", width=10,
               height=2, command=escribir_block)
b2_f2.place(x=1598, y=380)
window.mainloop()
