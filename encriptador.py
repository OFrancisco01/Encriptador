#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:11:39 2019

@author: watchdog
"""

from tkinter import *
from tkinter import messagebox

root = Tk()

def send():
    mensaje.set("Mensaje enviado")
    
variable = StringVar(root)
variable.set("128 bits") # default value

root.title("Encriptator 1.0")
root.iconbitmap("@hola.xbm")
root.geometry("500x400")

etiqueta1 = Label(root,text="Tipo transporte: ").place(x=20, y=20) 
radio1= Radiobutton(root, text="UDPO", value=1).place(x=20, y=50)
radio2= Radiobutton(root, text="TCP", value=1).place(x=80, y=50)

etiqueta2 = Label(root,text="Seleccion de cifrado: ").place(x=180, y=20) 
optionMenu=OptionMenu(root, variable, "128 bits","256 bits","clave publica/privada").place(x=180, y=50)

texto = Text(root,width=60, height=15 ).place(x=20, y=80)
#texto.config(width=30, height=10, font=("consolas",12),padx=15, pady=15,selectbackground="red")

boton = Button(root, text="Enviar", command=send ).place(x=20, y=260)


#Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left").place(x=10, y=380)


root.config(menu=menubar)
root.mainloop()

