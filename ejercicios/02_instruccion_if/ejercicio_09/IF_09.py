import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: León
apellido: Sokolowski
div: K
---
Ejercicio: instrucion_if_09
---
Al presionar el botón  'Calcular', se deberá mostrar (utilizando el Dialog alert) un número
aleatorio entre el 1 y el 10 inclusive
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_random = random.randint(1,10) #Se escribe desde que valor int hasta que otro.
        #numero_random = random.randrange(1,10)
        mensaje = f"El número aleatorio que le tocó fue {numero_random}"
        alert(title= "Ejercicio IF 09", message= mensaje)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()