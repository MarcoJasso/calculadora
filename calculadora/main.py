from tkinter import * 

# Establecer oniguración de la raiz 

raiz = Tk()

# variables
numerosSeleccionado = StringVar()
contenderNumeros = StringVar()
contenedorOperaciones = StringVar()

# definir constantes
w_ventana = 400
h_ventana = 400
font_text = "Arial Narrow"

x_ventana = raiz.winfo_screenwidth() // 2 - w_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - h_ventana // 2

posicion = str(w_ventana) + "x" + str(h_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)
raiz.resizable(0, 0)
raiz.iconbitmap("calculadora/assets/img/calculadora.ico")
raiz.title("Calculadora")

# Definicion de funciones

def mostrarNumero():
    raiz.show
    pass

# Establecer configuaración del WIDGET Frame como contenedor

contenedor = Frame(raiz, width=w_ventana, height=h_ventana)
contenedor.config(bg="white")
contenedor.pack()

# Configuración de los WIDGETs Label

lbl_contenedorOperaciones = Entry(contenedor, highlightthickness=2, textvariable=contenderNumeros)
lbl_contenedorOperaciones.config(justify=RIGHT, bg="white", font=(font_text, 12), border=0)
# lbl_contenedorOperaciones.config(highlightbackground = "#10C1C4", highlightcolor= "#C6FCFC")
lbl_contenedorOperaciones.place(x=10, y=21, width=380, height=30) 

lbl_contenedorNumeros = Entry(contenedor, highlightthickness=2)
lbl_contenedorNumeros.config(justify=RIGHT, bg="white", font=(font_text, 12), border=0)
# txt_contenedorNumeros.config(highlightbackground = "#10C1C4", highlightcolor= "#C6FCFC")
lbl_contenedorNumeros.place(x=10, y=50, width=380, height=30)

# Configuración de los WIDGETs Button

# Primera fila

btn_MC = Button(contenedor, text="MC", command=mostrarNumero)
btn_MC.place(width=40, height=40, y=100, x=10)
btn_MC.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_MR = Button(contenedor, text="MR")
btn_MR.place(width=40, height=40, y=100, x=60)
btn_MR.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_MMenos = Button(contenedor, text="M-")
btn_MMenos.place(width=40, height=40, y=100, x=110)
btn_MMenos.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_MMas = Button(contenedor, text="M+")
btn_MMas.place(width=40, height=40, y=100, x=160)
btn_MMas.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

# Segunda fila

btn_7 = Button(contenedor, text="7")
btn_7.place(width=40, height=40, y=150, x=10)
btn_7.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_8 = Button(contenedor, text="8")
btn_8.place(width=40, height=40, y=150, x=60)
btn_8.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_9 = Button(contenedor, text="9") 
btn_9.place(width=40, height=40, y=150, x=110)
btn_9.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_divicion = Button(contenedor, text="/")
btn_divicion.place(width=40, height=40, y=150, x=160)
btn_divicion.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

# Tercera fila

btn_4 = Button(contenedor, text="4")
btn_4.place(width=40, height=40, y=200, x=10)
btn_4.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_5 = Button(contenedor, text="5")
btn_5.place(width=40, height=40, y=200, x=60)
btn_5.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_6 = Button(contenedor, text="6")
btn_6.place(width=40, height=40, y=200, x=110)
btn_6.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_multi = Button(contenedor, text="*")
btn_multi.place(width=40, height=40, y=200, x=160)
btn_multi.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

# Cuarta fila

btn_1 = Button(contenedor, text="1")
btn_1.place(width=40, height=40, y=250, x=10)
btn_1.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_2 = Button(contenedor, text="2")
btn_2.place(width=40, height=40, y=250, x=60)
btn_2.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_3 = Button(contenedor, text="3")
btn_3.place(width=40, height=40, y=250, x=110)
btn_3.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_resta = Button(contenedor, text="-")
btn_resta.place(width=40, height=40, y=250, x=160)
btn_resta.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

# Quinta fila

btn_0 = Button(contenedor, text="0")
btn_0.place(width=40, height=40, y=250, x=10)
btn_0.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_punto = Button(contenedor, text=".")
btn_punto.place(width=40, height=40, y=250, x=60)
btn_punto.config(bd=0, bg="#D7D7D7", font=(font_text, 20))

btn_igual = Button(contenedor, text="=")
btn_igual.place(width=40, height=40, y=250, x=110)
btn_igual.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

btn_suma = Button(contenedor, text="+")
btn_suma.place(width=40, height=40, y=250, x=160)
btn_suma.config(bd=0, bg="#D7D7D7", font=(font_text, 12))

# Sexta fila

btn_AC = Button(contenedor, text="AC")
btn_AC.place(width=40, height=40, y=300, x=10)
btn_AC.config(bd=0, bg="#D7D7D7", font=(font_text, 12))



raiz.mainloop()
