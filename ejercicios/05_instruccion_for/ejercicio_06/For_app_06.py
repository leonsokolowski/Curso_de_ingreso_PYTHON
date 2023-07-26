import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: León
apellido: Sokolowski
div: K

Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt("Ejercicio For 06", "Ingrese hasta que número quiere contar"))
        numero = numero + 1
        contador = 0
        for i in range (0, numero, 2):
            alert(None, i)
            contador += 1
        
        contador = contador - 1
        mensaje = f"Se encontraron {contador} números pares"
        alert(None, mensaje)
                     
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()