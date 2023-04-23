from tkinter import *
from tkinter.font import BOLD

# Establecer oniguración de la raiz

raiz = Tk()

# Definicion de funciones

i = 0
cantidad_memoria = 0

def botonNumeroSeleccionado(numero):
    global i
    lbl_contenedorOperaciones.insert(i, numero)
    i+=1

def resultadoOperaciones():
    operacion = lbl_contenedorOperaciones.get()
    try:
        resultado = eval(operacion)
        lbl_contenedorResultado.delete(0, END)
        lbl_contenedorResultado.insert(0, resultado)
    except:
        lbl_contenedorResultado.delete(0, END)
        lbl_contenedorResultado.insert(0, " :: Math error ::  ")

def guardarEnMemoria(operacion):
    global cantidadMemoria
    
    
    valor = str(cantidadMemoria) + operacion + lbl_contenedorOperaciones.get()
    operacion = eval(valor)
    lbl_contenedorOperaciones.delete(0, END)

    cantidadMemoria = operacion

def borrarMemoria():
    global cantidadMemoria
    lbl_contenedorResultado.delete(0, END)
    lbl_contenedorResultado.insert(0, str(cantidadMemoria))
    cantidadMemoria = 0
    pass

def mostrarResultadoMemoria():
    global cantidadMemoria
    lbl_contenedorResultado.delete(0, END)
    lbl_contenedorResultado.insert(0, str(cantidadMemoria))


def borrarDatos():
    lbl_contenedorOperaciones.delete(0, END)
    lbl_contenedorResultado.delete(0, END)
    lbl_contenedorResultado.insert(0, "0")
# def _puntoDecimal():
 #    bandera = 0
 #    for item in auxiliarTemporal:
 #        if item == ".":
 #            bandera = 1
 #           break

  #   if bandera == 0:
  #       auxiliarTemporal.append(".")
  #       contenedorNumeros.set(auxiliarTemporal)


# variables de contenedores
contenedor_numeros = StringVar()
contenedor_resultado = StringVar()

# definir constantes
WIDTH_WINDOW = 400
HEIGHT_WINDOW = 400
FUENTE_TEXTO = "Arial Narrow"

x_ventana = raiz.winfo_screenwidth() // 2 - WIDTH_WINDOW // 2
y_ventana = raiz.winfo_screenheight() // 2 - HEIGHT_WINDOW // 2

posicion = str(WIDTH_WINDOW) + "x" + str(HEIGHT_WINDOW) + "+" + \
    str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)
# raiz.resizable(0, 0)
raiz.iconbitmap("./assets/img/calculadora.ico")

raiz.title("Calculadora")


# Establecer configuaración del WIDGET Frame como contenedor

contenedor = Frame(raiz, width=WIDTH_WINDOW, height=HEIGHT_WINDOW)
contenedor.config(bg="white")
contenedor.pack()

# Configuración de los WIDGETs Label

lbl_contenedorOperaciones = Entry(contenedor, highlightthickness=2, textvariable=contenedor_numeros)
lbl_contenedorOperaciones.config(justify=LEFT, bg="GRAY", fg="white", font=(FUENTE_TEXTO, 14, BOLD), border=0)
# lbl_contenedorOperaciones.config(highlightbackground = "#10C1C4", highlightcolor= "#C6FCFC")
lbl_contenedorOperaciones.place(x=10, y=21, width=380, height=30)

lbl_contenedorResultado = Entry(contenedor, highlightthickness=2, textvariable=contenedor_resultado)
lbl_contenedorResultado.config(justify=RIGHT, bg="gray", fg="white", font=(FUENTE_TEXTO, 16, BOLD), border=0)
# txt_contenedorResultado.config(highlightbackground = "#10C1C4", highlightcolor= "#C6FCFC")
lbl_contenedorResultado.place(x=10, y=50, width=380, height=30)

# Etiqueta para mostrar los datos en memoria

lbl_contenedorDatosMemoria = Label(contenedor)
lbl_contenedorDatosMemoria.config(justify=LEFT, bg="lightgray", fg="white", font=(FUENTE_TEXTO, 14, BOLD), border=0)
lbl_contenedorDatosMemoria.place(x=220, y=100, width=170, height=100)

# Configuración de los WIDGETs Button

# Primera fila

btn_MC = Button(contenedor, text="MC", command=borrarMemoria)
btn_MC.place(width=40, height=40, y=100, x=10)
btn_MC.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_MR = Button(contenedor, text="MR", command=mostrarResultadoMemoria)
btn_MR.place(width=40, height=40, y=100, x=60)
btn_MR.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_MMenos = Button(contenedor, text="M-", command=lambda:guardarEnMemoria("-"))
btn_MMenos.place(width=40, height=40, y=100, x=110)
btn_MMenos.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_MMas = Button(contenedor, text="M+", command=lambda:guardarEnMemoria("+"))
btn_MMas.place(width=40, height=40, y=100, x=160)
btn_MMas.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

# Segunda fila

btn_7 = Button(contenedor, text="7",
               command=lambda: botonNumeroSeleccionado("7"))
btn_7.place(width=40, height=40, y=150, x=10)
btn_7.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_8 = Button(contenedor, text="8",
               command=lambda: botonNumeroSeleccionado("8"))
btn_8.place(width=40, height=40, y=150, x=60)
btn_8.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_9 = Button(contenedor, text="9",
               command=lambda: botonNumeroSeleccionado("9"))
btn_9.place(width=40, height=40, y=150, x=110)
btn_9.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_divicion = Button(contenedor, text="/",
                      command=lambda: botonNumeroSeleccionado("/"))
btn_divicion.place(width=40, height=40, y=150, x=160)
btn_divicion.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

# Tercera fila

btn_4 = Button(contenedor, text="4",
               command=lambda: botonNumeroSeleccionado("4"))
btn_4.place(width=40, height=40, y=200, x=10)
btn_4.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_5 = Button(contenedor, text="5",
               command=lambda: botonNumeroSeleccionado("5"))
btn_5.place(width=40, height=40, y=200, x=60)
btn_5.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_6 = Button(contenedor, text="6",
               command=lambda: botonNumeroSeleccionado("6"))
btn_6.place(width=40, height=40, y=200, x=110)
btn_6.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_multi = Button(contenedor, text="*",
                   command=lambda: botonNumeroSeleccionado("*"))
btn_multi.place(width=40, height=40, y=200, x=160)
btn_multi.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

# Cuarta fila

btn_1 = Button(contenedor, text="1",
               command=lambda: botonNumeroSeleccionado("1"))
btn_1.place(width=40, height=40, y=250, x=10)
btn_1.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_2 = Button(contenedor, text="2",
               command=lambda: botonNumeroSeleccionado("2"))
btn_2.place(width=40, height=40, y=250, x=60)
btn_2.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_3 = Button(contenedor, text="3", command=lambda:botonNumeroSeleccionado("3"))
btn_3.place(width=40, height=40, y=250, x=110)
btn_3.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_resta = Button(contenedor, text="-", command=lambda:botonNumeroSeleccionado("-"))
btn_resta.place(width=40, height=40, y=250, x=160)
btn_resta.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

# Quinta fila

btn_0 = Button(contenedor, text="0", command=lambda:botonNumeroSeleccionado("0"))
btn_0.place(width=40, height=40, y=300, x=10)
btn_0.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_punto = Button(contenedor, text=".", command=lambda:botonNumeroSeleccionado("."))
btn_punto.place(width=40, height=40, y=300, x=60)
btn_punto.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 20))

btn_igual = Button(contenedor, text="=", command=resultadoOperaciones)
btn_igual.place(width=40, height=40, y=300, x=110)
btn_igual.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

btn_suma = Button(contenedor, text="+", command=lambda:botonNumeroSeleccionado("+"))
btn_suma.place(width=40, height=40, y=300, x=160)
btn_suma.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

# Sexta fila

btn_AC = Button(contenedor, text="AC", command=borrarDatos)
btn_AC.place(width=40, height=40, y=350, x=10)
btn_AC.config(bd=0, bg="#D7D7D7", font=(FUENTE_TEXTO, 12))

raiz.mainloop()
