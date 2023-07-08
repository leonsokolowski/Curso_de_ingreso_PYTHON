import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:León
apellido:Sokolowski
div: K
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #acá se usa prompt "title" y "prompt"
        nombre= prompt(title='Ingreso de un dato' , prompt='¿Cuál es tu nombre?')
        mensaje= "Tu nombre es " + nombre
        alert(title='Ejercicio E/S 02' , message=mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()